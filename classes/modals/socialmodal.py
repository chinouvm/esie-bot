import discord
from discord.ui import Modal, TextInput
from classes.embed import DefaultEmbed
from database import db


class SetSocialModal(Modal, title="⚜️Set your socials⚜️"):
    insta = TextInput(label="▫️Instagram", style=discord.TextStyle.short, required=True)
    snap = TextInput(label="▫️Snapchat", style=discord.TextStyle.short, required=True)
    spotify = TextInput(label="▫️Spotify (Optional)", style=discord.TextStyle.short, required=False)
    snaplink = TextInput(label="▫️Snaplink (Optional)(Use share link)", style=discord.TextStyle.long, required=False)

    async def on_submit(self, interaction: discord.Interaction):
        id = str(interaction.user)
        data = {"snapchat": self.snap.value, "insta": self.insta.value, "spotify": self.spotify.value, "snaplink": self.snaplink.value}
        db.collection("users").document(id).set(data)
        embed = DefaultEmbed(title="Succesfully set your socials", color=discord.Color.green())
        await interaction.response.send_message(embed=embed)
