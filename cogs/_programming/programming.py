from datetime import timedelta
from random import choice
import asyncpraw
from classes.embeds.embed import DefaultEmbed
from config import settings
import discord
from discord import app_commands
from discord.ext import commands
from guildlist import guildlist


class Programming(commands.Cog, app_commands.Group, name="programming"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        super().__init__()

    @app_commands.command(
        name="meme",
        description="Programming memes only",
    )
    @app_commands.checks.cooldown(1, 20, key=lambda i: (i.guild.id, i.user.id))
    async def meme(self, interaction: discord.Interaction):
        reddit = asyncpraw.Reddit(
            client_id=settings.REDDIT_CLIENTID, client_secret=settings.REDDIT_CLIENTSECRET, user_agent=settings.REDDIT_USERAGENT
        )

        subr = await reddit.subreddit("ProgrammerHumor")

        allsubr = []

        async for x in subr.hot(limit=50):
            allsubr.append(x)

        finalSub = choice(allsubr)

        embed = DefaultEmbed(color=discord.Color.from_rgb(67, 157, 254))
        embed.set_image(url=finalSub.url)
        await interaction.response.send_message(embed=embed)

    @meme.error
    async def commandSet_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            timeRemaining = str(timedelta(seconds=int(error.retry_after)))
            embed = DefaultEmbed(
                title=f"⛔ Error!",
                description=f"Please wait {timeRemaining} seconds before executing this command again!",
                color=discord.Color.from_rgb(255, 0, 0),
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(Programming(bot), guilds=guildlist)
