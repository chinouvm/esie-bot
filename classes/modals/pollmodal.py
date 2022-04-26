import discord
from discord.ui import Modal, TextInput
from classes.embeds.embed import DefaultEmbed


class PollCreation(Modal, title="Poll Creation"):
    vraag = TextInput(label="Vraag", style=discord.TextStyle.short, required=True)
    optie1 = TextInput(label="Optie 1", style=discord.TextStyle.short, required=True)
    optie1emoji = TextInput(label="Emoji voor optie 1", style=discord.TextStyle.short, required=True)
    optie2 = TextInput(label="Optie 2", style=discord.TextStyle.short, required=True)
    optie2emoji = TextInput(label="Emoji voor optie 2", style=discord.TextStyle.short, required=True)

    async def on_submit(self, interaction: discord.Interaction):
        embed = DefaultEmbed(title=f"Poll: {self.vraag.value}", color=discord.Color.from_rgb(67, 157, 254))
        embed.add_field(name=f"{self.optie1.value}", value=f"{self.optie1emoji.value}", inline=True)
        embed.add_field(name=f"{self.optie2.value}", value=f"{self.optie2emoji.value}", inline=True)
        await interaction.response.send_message(embed=embed)
