from random import randint, choice
import aiohttp
import discord
from discord import app_commands
from discord.ext import commands
import json

from classes.embed import DefaultEmbed
from config import settings


class Trash(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="trash", description="call a user trash")
    async def trash(self, interaction: discord.Interaction, member: discord.Member):
        search_terms = ["L", "Trash", "You're Bad", "You're Stupid", "Shitpost"]
        search_term = choice(search_terms)
        async with aiohttp.ClientSession() as session:
            async with session.get("https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, settings.TENORKEY, 20)) as response:
                data = json.loads(await response.text())
                randomNumber = randint(1, len(data["results"]))
                gif = data["results"][randomNumber]["media"][0]["gif"]["url"]
                embed = DefaultEmbed(title=f"{interaction.user.display_name} called {member.name} trash", color=discord.Color.magenta())
                embed.set_image(url=gif)
                await interaction.response.send_message(embed=embed)
                await session.close()


async def setup(bot: commands.Bot):
    await bot.add_cog(Trash(bot), guilds=[discord.Object(id=settings.SERVERID), discord.Object(id=settings.TESTSERVERID)])
