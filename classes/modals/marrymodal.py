import discord
from discord.ui import Modal, TextInput
from classes.embed import DefaultEmbed


class MarryModal(Modal, title="💍Proposal"):
    reason = TextInput(label="Proposal message", style=discord.TextStyle.long, required=True, max_length=1024)
    cutequote = TextInput(label="Cute quote (OPTIONAL)", style=discord.TextStyle.short, required=False)

    async def on_submit(self, interaction: discord.Interaction):
        embed = DefaultEmbed(title="Succesfully send proposal", color=discord.Color.green())
        await interaction.response.send_message(embed=embed)
