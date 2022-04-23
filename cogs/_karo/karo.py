import discord
from discord import app_commands
from discord.ext import commands
from guildlist import guildlist

from classes.embeds.embed import DefaultEmbed


class Karo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="karo", description="Use Karo powers to turn the bot off")
    async def karo(self, interaction: discord.Interaction):
        if interaction.user.id == 356188517635981322 or interaction.user.id == 213715321742295040:
            await interaction.response.send_message("Shutting down...")
            print("Shutting down...")
            await self.bot.close()
        else:
            embed = DefaultEmbed(
                title=f"⛔ Error!",
                description=f"You are not allowed to use this command!",
                color=discord.Color.from_rgb(255, 0, 0),
            )
            await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Karo(bot), guilds=guildlist)
