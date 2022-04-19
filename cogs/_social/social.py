from discord.ui import Button, View
import discord
from discord import app_commands
from discord.ext import commands

from classes.embed import DefaultEmbed
from classes.modals.socialmodal import SetSocialModal
from database import db
from config import settings


class Social(commands.Cog, name="Socials"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="setsocial",
        description="set your own socials",
    )
    async def setsocial(self, interaction: discord.Interaction):
        await interaction.response.send_modal(SetSocialModal())

    @app_commands.command(
        name="social",
        description="get socials",
    )
    async def social(self, interaction: discord.Interaction, member: discord.Member):
        id = str(member.id)
        print(id)
        userData = db.collection("users").document(id).get()
        if userData.exists:

            snapchat = userData.to_dict().get("snapchat")
            instagram = userData.to_dict().get("insta")
            spotify = userData.to_dict().get("spotify")
            snaplink = userData.to_dict().get("snaplink")
            github = userData.to_dict().get("github")

            view = View()
            embed = DefaultEmbed(title=f"Socials van {member.name}", color=discord.Color.from_rgb(67, 157, 254))
            if snaplink != None and len(snaplink) > 10:
                buttonSnap = Button(label="snap", style=discord.ButtonStyle.link, url=f"{snaplink}")
                view.add_item(buttonSnap)
            if spotify != None and len(spotify) > 3:
                buttonSpotify = Button(label="spotify", style=discord.ButtonStyle.link, url=f"https://open.spotify.com/user/{spotify}/")
                view.add_item(buttonSpotify)
                embed.add_field(name="Spotify", value=f"`{spotify}`", inline=False)
            if github != None and len(github) > 3:
                buttonSpotify = Button(label="github", style=discord.ButtonStyle.link, url=f"https://github.com/{github}")
                view.add_item(buttonSpotify)
                embed.add_field(name="Github", value=f"`{github}`", inline=False)

            buttonInsta = Button(label="insta", style=discord.ButtonStyle.link, url=f"https://www.instagram.com/{instagram}/")
            view.add_item(buttonInsta)

            embed.add_field(name="Instagram", value=f"`{instagram}`", inline=False)
            embed.add_field(name="Snapchat", value=f"`{snapchat}`", inline=False)
            embed.set_thumbnail(url=f"{member.avatar}")

            await interaction.response.send_message(view=view, embed=embed)
        else:
            embed = DefaultEmbed(title=f"Did not find {member.name} socials", color=discord.Color.red())
            await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Social(bot), guilds=[discord.Object(id=settings.SERVERID), discord.Object(id=settings.TESTSERVERID)])
