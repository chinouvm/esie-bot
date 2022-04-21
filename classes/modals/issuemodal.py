import discord
from discord.ui import Modal, TextInput
from classes.embed import DefaultEmbed


class PostIssue(Modal, title="❌ Github Issue ❌"):
    issuetitle = TextInput(label="Title", style=discord.TextStyle.short, required=True)
    issuebody = TextInput(label="Issue", style=discord.TextStyle.long, required=True)

    async def on_submit(self, interaction: discord.Interaction):
        embed = DefaultEmbed(title="Succesfully created a Github Issue", color=discord.Color.from_rgb(67, 157, 254))
        await interaction.response.send_message(embed=embed)
