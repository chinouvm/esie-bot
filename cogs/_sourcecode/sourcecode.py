import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import View, Button

from classes.embed import DefaultEmbed
from config import settings
from guildlist import guildlist


class SourceCode(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="sourcecode", description="Get source code")
    async def sourcecode(self, interaction: discord.Interaction):
        view = View()
        buttonSource = Button(emoji="🗂️", style=discord.ButtonStyle.link, url="https://github.com/chinouvm/esie-bot/")
        view.add_item(buttonSource)
        embed = DefaultEmbed(title="Source code of Esie Bot", color=discord.Color.from_rgb(67, 157, 254))
        await interaction.response.send_message(view=view, embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(SourceCode(bot), guilds=guildlist)
