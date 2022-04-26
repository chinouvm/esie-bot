from classes.embeds.embed import DefaultEmbed


class GifEmbed(DefaultEmbed):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = "Gif"
        self.add_field(name="**/gif search {value}**", value="`/gif search {value}` can be used to search for a gif.", inline=False)
        self.add_field(
            name="**/gif monkey**",
            value="`/gif monkey` Just monkey.",
            inline=False,
        )
