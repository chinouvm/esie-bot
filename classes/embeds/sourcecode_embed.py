from classes.embeds.embed import DefaultEmbed
from discord import Color


class SourceCodeEmbed(DefaultEmbed):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = Color.from_rgb(67, 157, 254)
        self.title = "Source Code of Esie Bot"
        self.add_field(name="**/sourcecode**", value="`/sourcecode` is used to get the source code of Esie Bot", inline=False)
