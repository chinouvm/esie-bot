import discord
from config import settings
from discord import app_commands
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="ping",
        description="Returns the latency of the bot.")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'🏓 Pong! {round(self.bot.latency * 1000)}ms')


async def setup(bot: commands.Bot):
    await bot.add_cog(
        Ping(bot),
        guilds=[discord.Object(id=settings.TESTSERVERID), discord.Object(id=settings.SERVERID)])
