import discord
from discord.ui import View
from discord import SelectOption
from classes.modals.socialmodal import UpdateSocialModal
from database import db


async def UpdateSocial(id, social: str, value: str):
    data = {social: str(value)}
    db.collection("users").document(str(id)).update(data)


class UpdateSocialView(View):
    @discord.ui.select(
        options=[
            SelectOption(label="Instagram", value="insta"),
            SelectOption(label="Snapchat", value="snap"),
            SelectOption(label="Spotify", value="spotify"),
            SelectOption(label="Snaplink", value="snaplink"),
            SelectOption(label="Github", value="github"),
        ]
    )
    async def select_callback(self, interaction, select):
        modal = UpdateSocialModal(title="Update your socials")
        await interaction.response.send_modal(modal)
        await modal.wait()

        if select.values[0] == "insta":
            await UpdateSocial(interaction.user.id, "insta", modal.updated.value)
        elif select.values[0] == "snap":
            await UpdateSocial(interaction.user.id, "snapchat", modal.updated.value)
        elif select.values[0] == "spotify":
            await UpdateSocial(interaction.user.id, "spotify", modal.updated.value)
        elif select.values[0] == "snaplink":
            await UpdateSocial(interaction.user.id, "snaplink", modal.updated.value)
        elif select.values[0] == "github":
            await UpdateSocial(interaction.user.id, "github", modal.updated.value)

        select.disabled = True
        await interaction.message.edit(view=self)
