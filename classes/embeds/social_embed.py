from classes.embeds.embed import DefaultEmbed
from discord import Color


class SocialEmbed(DefaultEmbed):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = "Social"
        self.color = Color.from_rgb(67, 157, 254)
        self.add_field(
            name="**/social set**", value="`/social set` can be used to set your socials. (snapchat, instagram, github, spotify)", inline=False
        )
        self.add_field(
            name="**/social update**",
            value="`/social update` is used to update your socials. Update will send you a dm where you can select the type of platform you want to update.",
            inline=False,
        )
        self.add_field(
            name="**/social get {member}**",
            value="`/social get {member}` is used to get the socials of a user.",
            inline=False,
        )
