from classes.embeds.embed import DefaultEmbed


class TrashEmbed(DefaultEmbed):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = "🔧Trash🔧"
        self.add_field(name="**/trash {member}**", value="`/trash {member}` can be used to trash talk a user with a gif.", inline=False)
