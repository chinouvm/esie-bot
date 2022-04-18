from time import time
import discord
from config import settings
from discord import app_commands
from discord.ext import commands
from database import db


class Code(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="code",
        description="Return total time spend coding inside vscode")
    async def code(self, interaction: discord.Interaction):
        id = str(interaction.user.name)
        results = db.collection(u'users').document(id).get()
        if results.exists:
            total = results.to_dict()['totalminutes']
        await interaction.response.send_message(f'{id} has spent {round(total)} minutes coding in vscode.')


async def setup(bot: commands.Bot):
    await bot.add_cog(
        Code(bot),
        guilds=[discord.Object(id=settings.TESTSERVERID), discord.Object(id=settings.SERVERID)])
