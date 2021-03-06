from datetime import datetime
from config import settings
import discord
from discord.ext import commands


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=discord.Intents.all(),
            application_id=settings.APPID,
            activity=discord.Activity(type=discord.ActivityType.watching, name="esie.nl | v1.0.0"),
        )

    async def setup_hook(self):
        await self.load_extension(f"cogs._status.status")
        await self.load_extension(f"cogs._git.git")
        await self.load_extension(f"cogs._social.social")
        await self.load_extension(f"cogs._wgn.wgn")
        await self.load_extension(f"cogs._sourcecode.sourcecode")
        await self.load_extension(f"cogs._trash.trash")
        await self.load_extension(f"cogs._help.help")
        await self.load_extension(f"cogs._karo.karo")
        await self.load_extension(f"cogs._gif.gif")
        await self.load_extension(f"cogs._programming.programming")
        await self.load_extension(f"cogs._poll.poll")
        await bot.tree.sync(guild=discord.Object(id=959010133273370664))  # Esie
        await bot.tree.sync(guild=discord.Object(id=860153924899176478))  # WGN
        # await bot.tree.sync(guild=discord.Object(id=968553036244987914))  # Dev

        bot.remove_command("help")

    async def on_ready(self):
        print(f"{self.user} Initialised {datetime.now()}")


bot = MyBot()
bot.run(settings.TOKEN)
