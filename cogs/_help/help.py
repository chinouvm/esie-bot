import discord
from discord import app_commands
from discord.ext import commands

from classes.embeds.help_embed import HelpEmbed
from classes.views.helpview import HelpView
from guildlist import guildlist


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="help", description="pls help")
    async def help(self, interaction: discord.Interaction):
        await interaction.response.send_message(embed=HelpEmbed(), view=HelpView(), ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(Help(bot), guilds=guildlist)
