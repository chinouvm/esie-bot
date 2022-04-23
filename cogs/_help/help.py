import discord
from discord import app_commands
from discord.ext import commands

from classes.embeds.embed import DefaultEmbed
from classes.views.helpview import HelpView
from guildlist import guildlist


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="help", description="pls help")
    async def help(self, interaction: discord.Interaction):
        embed = DefaultEmbed(title="⚠️Help Menu⚠️", color=discord.Color.from_rgb(67, 157, 254))
        embed.description = "The Esie Bot is a bot that is used to help you with various things.\n These commands are still under development and may contain bugs. \n If you encounter error or get an unexpected response from the bot make sure to use `/git issue` to let the developers know whats wrong <3 \n\n The following are the commands that are available:\n"
        embed.add_field(name="*List of Commands*", value="`Source Code`\n`W.G.N Discord`\n`Social`\n`Gif`\n`Trash`\n`Git`\n`Status`", inline=False)
        embed.set_thumbnail(url=self.bot.user.avatar)
        await interaction.response.send_message(embed=embed, view=HelpView())


async def setup(bot: commands.Bot):
    await bot.add_cog(Help(bot), guilds=guildlist)
