import discord
from discord.ui import Modal, TextInput
from classes.embeds.embed import DefaultEmbed
from database import db


class SetSocialModal(Modal, title="⚜️Set your socials⚜️"):
    insta = TextInput(label="▫️Instagram", style=discord.TextStyle.short, required=True)
    snap = TextInput(label="▫️Snapchat", style=discord.TextStyle.short, required=True)
    spotify = TextInput(label="▫️Spotify (Optional)", style=discord.TextStyle.short, required=False)
    github = TextInput(label="Github (Optional)", style=discord.TextStyle.short, required=False)
    snaplink = TextInput(label="▫️Snaplink (Optional)(Use share link)", style=discord.TextStyle.long, required=False)

    async def on_submit(self, interaction: discord.Interaction):
        id = str(interaction.user.id)
        data = {
            "snapchat": self.snap.value,
            "insta": self.insta.value,
            "spotify": self.spotify.value,
            "snaplink": self.snaplink.value,
            "github": self.github.value,
        }
        db.collection("users").document(id).set(data)
        embed = DefaultEmbed(title="Succesfully set your socials", color=discord.Color.from_rgb(67, 157, 254))
        await interaction.response.send_message(embed=embed, ephemeral=True)


class UpdateSocialModal(Modal, title="⚜️Update your socials⚜️"):
    updated = TextInput(label="Enter a new value", style=discord.TextStyle.short, required=True)

    async def on_submit(self, interaction: discord.Interaction):
        embed = DefaultEmbed(title="Succesfully updated your socials", color=discord.Color.from_rgb(67, 157, 254))
        await interaction.response.send_message(embed=embed, ephemeral=True)
