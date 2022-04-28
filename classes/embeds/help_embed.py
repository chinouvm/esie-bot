from classes.embeds.embed import DefaultEmbed
from discord import Color


class HelpEmbed(DefaultEmbed):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = "⚠️Help Menu⚠️"
        self.color = Color.from_rgb(67, 157, 254)
        self.description = "The Esie Bot is a bot that is used to help you with various things.\n These commands are still under development and may contain bugs. \n If you encounter error or get an unexpected response from the bot make sure to use `/git issue` to let the developers know whats wrong <3 \n\n The submenu's are available:\n"
        self.add_field(
            name="*List of submenu's*",
            value="`- Source Code`\n`- W.G.N Discord`\n`- Social`\n`- Gif`\n`- Trash`\n`- Git`\n`- Status`\n`- Programming`",
            inline=False,
        )
