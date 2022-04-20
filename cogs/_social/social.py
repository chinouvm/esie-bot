from discord.ui import Button, View
import discord
from discord import Embed, app_commands

from classes.views.updatesocialview import UpdateSocialView
from discord.ext import commands

from classes.embed import DefaultEmbed
from classes.modals.socialmodal import SetSocialModal
from database import db
from config import settings


class Social(commands.Cog, app_commands.Group, name="social"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        super().__init__()

    @app_commands.command(
        name="set",
        description="set your own socials",
    )
    async def set(self, interaction: discord.Interaction):
        await interaction.response.send_modal(SetSocialModal())

    @app_commands.command(
        name="get",
        description="get socials",
    )
    @app_commands.describe(member="The username of the member you want to get socials from")
    async def get(self, interaction: discord.Interaction, member: discord.Member):
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

    @app_commands.command(
        name="update",
        description="update your socials",
    )
    async def update(self, interaction: discord.Interaction):

        await interaction.user.send(
            view=UpdateSocialView(), embed=Embed(title=f"Select a social platform to update", color=discord.Color.from_rgb(67, 157, 254))
        )

        await interaction.response.send_message(
            embed=Embed(title=f"{interaction.user.display_name} recieved a update message ", color=discord.Color.from_rgb(67, 157, 254))
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(
        Social(bot),
        guilds=[
            discord.Object(id=settings.TESTSERVERID),
            discord.Object(id=settings.SERVERID),
        ],
    )
