import discord
from discord import app_commands
from discord.ext import commands

from classes.embed import DefaultEmbed
from config import settings


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="help", description="pls help")
    async def help(self, interaction: discord.Interaction):
        embed = DefaultEmbed(title="Help Menu", color=discord.Color.from_rgb(67, 157, 254))
        embed.add_field(name="Source code", value="Use `sourcecode` command to get Esie source code", inline=True)
        embed.add_field(name="W.G.N", value="Use `wgn` command to get W.G.N discord invite link", inline=True)
        embed.add_field(name="Help", value="Use `help` command to get this message", inline=True)
        embed.add_field(name="Marry", value="Use `marry` command to get a proposal", inline=True)
        embed.add_field(name="Social", value="Use `social` command to get social commands", inline=True)
        embed.add_field(name="Trash", value="Use `trash` command to call a user trash", inline=True)
        embed.add_field(name="Status", value="Use `status` command see the latency of the bot and the status of the website", inline=True)
        embed.add_field(name="Git User", value="Use `git user` command to retrieve information about a github user", inline=True)
        embed.add_field(
            name="Git Issue",
            value="Use `git issue` command to create a issue when there are bugs or you have suggestions",
            inline=True,
        )
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(
        Help(bot),
        guilds=[
            discord.Object(id=settings.SERVERID),
            discord.Object(id=settings.TESTSERVERID),
            discord.Object(id=settings.JIMSERVERID),
        ],
    )
