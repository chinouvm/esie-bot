from classes.embeds.embed import DefaultEmbed
from discord import Color


class GitEmbed(DefaultEmbed):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = "Git"
        self.color = Color.from_rgb(67, 157, 254)
        self.add_field(
            name="**/git user {username}**",
            value="`/git user {username}` can be used to search for a member on git and will return data from that user.",
            inline=False,
        )
        self.add_field(
            name="**/git issue**",
            value="`/git issue` is used to make a issue to give feedback or report a bug.",
            inline=False,
        )
