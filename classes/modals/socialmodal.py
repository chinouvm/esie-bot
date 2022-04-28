import discord
from discord.ui import Modal, TextInput
from classes.embeds.embed import DefaultEmbed
from database import db


async def SetSocial(id, data):
    try:
        db.collection("users").document(str(id)).set(data)
        return True
    except:
        return False


class SetSocialModal(Modal, title="⚜️Set your socials⚜️"):

    insta = TextInput(label="▫️Instagram", style=discord.TextStyle.short, required=True)
    snap = TextInput(label="▫️Snapchat", style=discord.TextStyle.short, required=True)
    spotify = TextInput(label="▫️Spotify (Optional)", style=discord.TextStyle.short, required=False)
    github = TextInput(label="Github (Optional)", style=discord.TextStyle.short, required=False)
    snaplink = TextInput(label="▫️Snaplink (Optional)(Use share link)", style=discord.TextStyle.long, required=False)

    async def on_submit(self, interaction: discord.Interaction):
        data = {
            "snapchat": self.snap.value,
            "insta": self.insta.value,
            "spotify": self.spotify.value,
            "snaplink": self.snaplink.value,
            "github": self.github.value,
        }
        if await SetSocial(interaction.user.id, data=data):
            await interaction.response.send_message(
                embed=DefaultEmbed(
                    title="✅ Socials set!", description="Your socials have been set!", color=discord.Color.from_rgb(67, 157, 254), ephemeral=True
                )
            )
        else:
            await interaction.response.send_message(
                embed=DefaultEmbed(
                    title="❌ Error!", description="Something went wrong, please try again later.", color=discord.Color.red(), ephemeral=True
                )
            )


class UpdateSocialModal(Modal, title="⚜️Update your socials⚜️"):
    updated = TextInput(label="Enter a new value", style=discord.TextStyle.short, required=True)

    async def on_submit(self, interaction: discord.Interaction):
        embed = DefaultEmbed(title="Succesfully updated your socials", color=discord.Color.from_rgb(67, 157, 254))
        await interaction.response.send_message(embed=embed, ephemeral=True)
