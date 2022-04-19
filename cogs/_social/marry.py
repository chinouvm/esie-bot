import discord
from discord import app_commands
from discord.ext import commands

from classes.embed import DefaultEmbed
from classes.modals.marrymodal import MarryModal
from config import settings


class Marry(commands.Cog, name="Marry"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="marry",
        description="marry your second half <3",
    )
    async def marry(self, interaction: discord.Interaction, member: discord.Member):
        modal = MarryModal()
        await interaction.response.send_modal(modal)
        await modal.wait()
        embed = DefaultEmbed(title=f"💍**{interaction.user.display_name}**💍 has proposed to you.", color=discord.Color.from_rgb(67, 157, 254))
        embed.add_field(name="❤️ Reason ❤️", value=f"{modal.reason.value}", inline=True)
        await member.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Marry(bot), guilds=[discord.Object(id=settings.SERVERID), discord.Object(id=settings.TESTSERVERID)])
