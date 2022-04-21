import aiohttp
import discord
from config import settings
from discord import app_commands
from discord.ext import commands
from classes.embed import DefaultEmbed
from guildlist import guildlist


class Status(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="status",
        description="Returns the latency of the bot and the status of the website",
    )
    async def status(self, interaction: discord.Interaction):
        embed = DefaultEmbed(title=f"Status", color=discord.Color.from_rgb(67, 157, 254))
        embed.add_field(name="Ping:", value=f"{round(self.bot.latency * 1000)}ms", inline=True)
        async with aiohttp.ClientSession() as session:
            async with session.get("https://www.esie.nl") as resp:
                if resp != None:
                    embed.add_field(name="Website: ", value=f"Online ✅", inline=True)
                else:
                    embed.add_field(name="Website: ", value=f"Offline ❌", inline=True)
            embed.set_thumbnail(url=f"{self.bot.user.avatar}")
            await interaction.response.send_message(embed=embed)
            await session.close()


async def setup(bot: commands.Bot):
    await bot.add_cog(Status(bot), guilds=guildlist)
