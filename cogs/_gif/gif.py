from array import array
from datetime import timedelta
import aiohttp
import discord
from classes.embeds.embed import DefaultEmbed
from config import settings
from discord import app_commands
from discord.ext import commands
from guildlist import guildlist
from random import randint
from random import choice
import aiohttp
import discord
from discord import app_commands
from discord.ext import commands
import json

from classes.embeds.embed import DefaultEmbed
from config import settings
from guildlist import guildlist


class Gif(commands.Cog, app_commands.Group, name="gif"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        super().__init__()

    async def getGif(searchTerm, amountOfTries: int, array: bool):
        if array:
            search_terms = searchTerm
            search_term = choice(search_terms)
        else:
            search_term = searchTerm
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, settings.TENORKEY, amountOfTries)
            ) as response:
                data = json.loads(await response.text())
                randomNumber = randint(1, len(data["results"]))
                gif = data["results"][randomNumber]["media"][0]["gif"]["url"]
                await session.close()
                return gif

    @app_commands.command(
        name="monkey",
        description="monkey",
    )
    @app_commands.checks.cooldown(1, 10, key=lambda i: (i.guild.id, i.user.id))
    async def monkey(self, interaction: discord.Interaction):
        embed = DefaultEmbed(title=f"{interaction.user.display_name} called for a monkey", color=discord.Color.from_rgb(67, 157, 254))
        embed.set_image(url=await Gif.getGif(searchTerm=["monkey", "Gibbons", "Chimpanse", "Gorilla"], amountOfTries=10, array=True))
        await interaction.response.send_message(embed=embed)

    @monkey.error
    async def command_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            timeRemaining = str(timedelta(seconds=int(error.retry_after)))
            embed = DefaultEmbed(
                title=f"⛔ Error!",
                description=f"Please wait {timeRemaining} seconds before executing this command again!",
                color=discord.Color.from_rgb(255, 0, 0),
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(
        name="search",
        description="search for a gif",
    )
    @app_commands.checks.cooldown(1, 10, key=lambda i: (i.guild.id, i.user.id))
    async def search(self, interaction: discord.Interaction, search_term: str):
        embed = DefaultEmbed(color=discord.Color.from_rgb(67, 157, 254))
        embed.set_image(url=await Gif.getGif(searchTerm=search_term, amountOfTries=10, array=False))
        await interaction.response.send_message(embed=embed)

    @search.error
    async def command_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            timeRemaining = str(timedelta(seconds=int(error.retry_after)))
            embed = DefaultEmbed(
                title=f"⛔ Error!",
                description=f"Please wait {timeRemaining} seconds before executing this command again!",
                color=discord.Color.from_rgb(255, 0, 0),
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(Gif(bot), guilds=guildlist)
