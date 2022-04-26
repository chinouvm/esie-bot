from discord.ui import Button, View
import discord
from discord import Embed, app_commands

from classes.views.updatesocialview import UpdateSocialView
from discord.ext import commands
from datetime import timedelta

from classes.embeds.embed import DefaultEmbed
from classes.modals.socialmodal import SetSocialModal
from database import db
from guildlist import guildlist


class Social(commands.Cog, app_commands.Group, name="social"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        super().__init__()

    @app_commands.command(
        name="set",
        description="set your own socials",
    )
    @app_commands.checks.cooldown(1, 60, key=lambda i: (i.guild.id, i.user.id))
    async def set(self, interaction: discord.Interaction):
        await interaction.response.send_modal(SetSocialModal(), ephemeral=True)

    @set.error
    async def commandSet_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            timeRemaining = str(timedelta(seconds=int(error.retry_after)))
            embed = DefaultEmbed(
                title=f"⛔ Error!",
                description=f"Please wait {timeRemaining} seconds before executing this command again!",
                color=discord.Color.from_rgb(255, 0, 0),
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(
        name="get",
        description="get socials",
    )
    @app_commands.describe(member="The username of the member you want to get socials from")
    @app_commands.checks.cooldown(1, 20, key=lambda i: (i.guild.id, i.user.id))
    async def get(self, interaction: discord.Interaction, member: discord.Member):
        id = str(member.id)
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
            embed = DefaultEmbed(title=f"Did not find {member.name} socials", color=discord.Color.from_rgb(255, 0, 0))
            await interaction.response.send_message(embed=embed, ephemeral=True)

    @get.error
    async def commandGet_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            timeRemaining = str(timedelta(seconds=int(error.retry_after)))
            embed = DefaultEmbed(
                title=f"⛔ Error!",
                description=f"Please wait {timeRemaining} seconds before executing this command again!",
                color=discord.Color.from_rgb(255, 0, 0),
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(
        name="update",
        description="update your socials",
    )
    @app_commands.checks.cooldown(1, 60, key=lambda i: (i.guild.id, i.user.id))
    async def update(self, interaction: discord.Interaction):

        await interaction.user.send(
            view=UpdateSocialView(), embed=Embed(title=f"Select a social platform to update", color=discord.Color.from_rgb(67, 157, 254))
        )

        await interaction.response.send_message(embed=Embed(title=f"Updating socials", color=discord.Color.from_rgb(67, 157, 254)), ephemeral=True)

    @update.error
    async def commandUpdate_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            timeRemaining = str(timedelta(seconds=int(error.retry_after)))
            embed = DefaultEmbed(
                title=f"⛔ Error!",
                description=f"Please wait {timeRemaining} seconds before executing this command again!",
                color=discord.Color.from_rgb(255, 0, 0),
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(Social(bot), guilds=guildlist)
