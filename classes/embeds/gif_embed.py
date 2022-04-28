from classes.embeds.embed import DefaultEmbed
from discord import Color


class GifEmbed(DefaultEmbed):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = "Gif"
        self.color = Color.from_rgb(67, 157, 254)
        self.add_field(name="**/gif search {value}**", value="`/gif search {value}` can be used to search for a gif.", inline=False)
        self.add_field(
            name="**/gif monkey**",
            value="`/gif monkey` Just monkey.",
            inline=False,
        )
