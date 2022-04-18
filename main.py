from time import time
from cogs.codes.checkcode import BackgroundTasks
from config import settings
import discord
from discord.ext import commands, tasks


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='!',
            intents=discord.Intents.all(),
            application_id='965233241600700457',
            activity=discord.Activity(
                type=discord.ActivityType.watching, name="www.esie.nl")
        )

    async def setup_hook(self):
        await self.load_extension(f'cogs.pings.ping')
        await self.load_extension(f'cogs.codes.code')
        await bot.tree.sync(guild=discord.Object(id=settings.TESTSERVERID))
        await bot.tree.sync(guild=discord.Object(id=settings.SERVERID))

    async def on_ready(self):
        self.guild = bot.get_guild(settings.SERVERID)
        print(f'{self.user} Initialised.')
        BackgroundTasks.check.start(self.guild)


bot = MyBot()
bot.run(settings.TOKEN)
