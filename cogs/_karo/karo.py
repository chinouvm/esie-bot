import discord
from discord import app_commands
from discord.ext import commands
from guildlist import guildlist


class Karo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="karo", description="Shutdown the bot")
    async def karo(self, interaction: discord.Interaction):
        await interaction.response.send_message("Shutting down...")
        print("Shutting down...")
        await self.bot.close()


async def setup(bot: commands.Bot):
    await bot.add_cog(Karo(bot), guilds=guildlist)
