import discord
from discord.ui import View
from discord import SelectOption

from classes.embeds.embed import DefaultEmbed
from classes.embeds.gif_embed import GifEmbed
from classes.embeds.git_embed import GitEmbed
from classes.embeds.help_embed import HelpEmbed
from classes.embeds.programming_embed import ProgrammingEmbed
from classes.embeds.social_embed import SocialEmbed
from classes.embeds.sourcecode_embed import SourceCodeEmbed
from classes.embeds.status_embed import StatusEmbed
from classes.embeds.trash_embed import TrashEmbed
from classes.embeds.wgn_embed import WGNEmbed


class HelpView(View):
    @discord.ui.select(
        placeholder="Select a helpmenu",
        options=[
            SelectOption(label="Main Menu", value="0"),
            SelectOption(label="- Source Code", value="1"),
            SelectOption(label="- W.G.N Discord", value="2"),
            SelectOption(label="- Social", value="3"),
            SelectOption(label="- Gif", value="4"),
            SelectOption(label="- Trash", value="5"),
            SelectOption(label="- Git", value="6"),
            SelectOption(label="- Status", value="7"),
            SelectOption(label="- Programming", value="8"),
        ],
    )
    async def select_callback(self, interaction, select):
        if select.values[0] == "0":
            await interaction.response.edit_message(embed=HelpEmbed())
        if select.values[0] == "1":
            await interaction.response.edit_message(embed=SourceCodeEmbed())
        elif select.values[0] == "2":
            await interaction.response.edit_message(embed=WGNEmbed())
        elif select.values[0] == "3":
            await interaction.response.edit_message(embed=SocialEmbed())
        elif select.values[0] == "4":
            await interaction.response.edit_message(embed=GifEmbed())
        elif select.values[0] == "5":
            await interaction.response.edit_message(embed=TrashEmbed())
        elif select.values[0] == "6":
            await interaction.response.edit_message(embed=GitEmbed())
        elif select.values[0] == "7":
            await interaction.response.edit_message(embed=StatusEmbed())
        elif select.values[0] == "8":
            await interaction.response.edit_message(embed=ProgrammingEmbed())
