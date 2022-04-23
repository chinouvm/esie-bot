import json
from random import choice, randint
import aiohttp
import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import View, Button

from classes.embeds.embed import DefaultEmbed
from config import Settings
from guildlist import guildlist


class WGN(commands.Cog, app_commands.Group, name="wgn"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        super().__init__()

    @app_commands.command(name="discord", description="get W.G.N discord invite link")
    async def wgn(self, interaction: discord.Interaction):
        view = View()
        buttonSource = Button(emoji="❤️", style=discord.ButtonStyle.link, url="https://discord.gg/YJk68J5qsJ")
        view.add_item(buttonSource)
        embed = DefaultEmbed(title="W.G.N Discord", color=discord.Color.from_rgb(67, 157, 254))
        embed.description = f"{interaction.user} Invited you to join W.G.N Discord"
        await interaction.response.send_message(view=view, embed=embed)

    @app_commands.command(name="lore", description="get W.G.N lore")
    async def lore(self, interaction: discord.Interaction):
        embed = DefaultEmbed(title="W.G.N Discord Lore", color=discord.Color.from_rgb(67, 157, 254))
        embed.description = f"{interaction.user} W.G.N Lore is not available yet"
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(WGN(bot), guilds=guildlist)
