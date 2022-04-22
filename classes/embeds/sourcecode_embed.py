from classes.embeds.embed import DefaultEmbed


class SourceCodeEmbed(DefaultEmbed):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = "📦 Source Code of Esie Bot"
        self.add_field(name="**/sourcecode**", value="`/sourcecode` is used to get the source code of Esie Bot", inline=False)
