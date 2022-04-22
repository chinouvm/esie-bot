from classes.embeds.embed import DefaultEmbed


class StatusEmbed(DefaultEmbed):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = "🔧Status of Esie🔧"
        self.add_field(name="**/status**", value="`/status` is used to get the status of Esie.", inline=False)
