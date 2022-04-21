import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import View, Button

from classes.embed import DefaultEmbed
from config import settings
from guildlist import guildlist


class WGN(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="wgn", description="get W.G.N discord invite link")
    async def wgn(self, interaction: discord.Interaction):
        view = View()
        buttonSource = Button(emoji="❤️", style=discord.ButtonStyle.link, url="https://discord.gg/YJk68J5qsJ")
        view.add_item(buttonSource)
        embed = DefaultEmbed(title="W.G.N Discord", color=discord.Color.from_rgb(67, 157, 254))
        embed.description = f"{interaction.user} Invited you to join W.G.N Discord"
        await interaction.response.send_message(view=view, embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(WGN(bot), guilds=guildlist)
