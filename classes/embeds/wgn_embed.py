from classes.embeds.embed import DefaultEmbed
from discord import Color


class WGNEmbed(DefaultEmbed):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = Color.from_rgb(67, 157, 254)
        self.title = "W.G.N Discord"
        self.add_field(name="**/wgn lore**", value="`/wgn lore` can be used to view the lore of the W.G.N. Discord Server", inline=False)
        self.add_field(name="**/wgn discord**", value="`/wgn discord` is used to get the invite link of the W.G.N. Discord Server", inline=False)
