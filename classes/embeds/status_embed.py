from classes.embeds.embed import DefaultEmbed
from discord import Color


class StatusEmbed(DefaultEmbed):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = Color.from_rgb(67, 157, 254)
        self.title = "Status of Esie"
        self.add_field(name="**/status**", value="`/status` is used to get the status of Esie.", inline=False)
