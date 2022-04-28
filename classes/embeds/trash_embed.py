from classes.embeds.embed import DefaultEmbed
from discord import Color


class TrashEmbed(DefaultEmbed):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = Color.from_rgb(67, 157, 254)
        self.title = "Trash"
        self.add_field(name="**/trash {member}**", value="`/trash {member}` can be used to trash talk a user with a gif.", inline=False)
