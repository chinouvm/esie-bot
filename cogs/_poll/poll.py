from operator import truediv
import discord
from discord import app_commands
from discord.ext import commands
from classes.modals.pollmodal import PollCreation
from guildlist import guildlist


class Poll(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="poll", description="Create a poll with reactions")
    async def poll(self, interaction: discord.Interaction):
        await interaction.response.send_modal(PollCreation())


async def setup(bot: commands.Bot):
    await bot.add_cog(Poll(bot), guilds=guildlist)
