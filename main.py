from time import time
from config import settings
import discord
from discord.ext import commands, tasks


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=discord.Intents.all(),
            application_id="965233241600700457",
            activity=discord.Activity(type=discord.ActivityType.watching, name="www.esie.nl"),
        )

    async def setup_hook(self):
        await self.load_extension(f"cogs.status.status")
        await self.load_extension(f"cogs.gits.git")
        await bot.tree.sync(guild=discord.Object(id=settings.TESTSERVERID))
        await bot.tree.sync(guild=discord.Object(id=settings.SERVERID))

    async def on_ready(self):
        print(f"{self.user} Initialised.")


bot = MyBot()
bot.run(settings.TOKEN)
