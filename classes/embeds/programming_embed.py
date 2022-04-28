from classes.embeds.embed import DefaultEmbed
from discord import Color


class ProgrammingEmbed(DefaultEmbed):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = "Programming"
        self.color = Color.from_rgb(67, 157, 254)
        self.add_field(name="**/programming meme**", value="`/programming meme` can be used to get a random meme about programming.", inline=False)
