from datetime import datetime
from config import settings
import discord
from discord.ext import commands


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=discord.Intents.all(),
            application_id="966745674941087745",
            activity=discord.Activity(type=discord.ActivityType.watching, name="www.esie.nl"),
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
        await bot.tree.sync(guild=discord.Object(id=860153924899176478))
        await bot.tree.sync(guild=discord.Object(id=959010133273370664))

        bot.remove_command("help")

    async def on_ready(self):
        print(f"{self.user} Initialised {datetime.now()}")


bot = MyBot()
bot.run(settings.TOKEN)
