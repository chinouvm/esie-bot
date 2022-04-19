import aiohttp
import discord
from classes.embed import DefaultEmbed
from config import settings
from discord import app_commands
from discord.ext import commands
from discord.ui import View, Button


class User:
    async def getUser(username):
        """ "Get user from github api"""
        headers = {"Authorization": f"token {settings.GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.github.com/users/{username}", headers=headers) as resp:
                body = await resp.json()
                return body


class Git(commands.Cog, app_commands.Group, name="git"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        super().__init__()

    @app_commands.command(
        name="user",
        description="Returns information about a certain github user",
    )
    @app_commands.describe(username="The username of the github user you want to get information about")
    async def user(self, interaction: discord.Interaction, username: str):
        try:
            body = await User.getUser(username)
            view = View()
            profileButton = Button(emoji="👤", style=discord.ButtonStyle.link, url=f"https://github.com/{username}")
            view.add_item(profileButton)
            embed = DefaultEmbed(title=f"Github Profile Info", color=discord.Color.from_rgb(67, 157, 254))
            embed.add_field(name="Username:", value=f"{body.get('login')}", inline=True)
            embed.add_field(name="Location:", value=f"{body.get('location')}", inline=True)
            embed.add_field(name="Followers:", value=f"{body.get('followers')}", inline=True)
            embed.add_field(name="Following:", value=f"{body.get('following')}", inline=True)
            embed.add_field(name="Public Repos:", value=f"{body.get('public_repos')}", inline=True)
            embed.set_thumbnail(url=f"{body.get('avatar_url')}")
            await interaction.response.send_message(view=view, embed=embed)
        except:
            embed = DefaultEmbed(title=f"⛔ Error!", description=f"Ongeldige gebruikersnaam!", color=discord.Color.from_rgb(255, 0, 0))
            await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(
        Git(bot),
        guilds=[
            discord.Object(id=settings.TESTSERVERID),
            discord.Object(id=settings.SERVERID),
        ],
    )
