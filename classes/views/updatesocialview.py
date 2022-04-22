import discord
from discord.ui import View
from discord import SelectOption
from classes.modals.socialmodal import UpdateSocialModal
from database import db


async def update_social(id, social, value):
    data = {social: value}
    await db.collection("users").document(id).update(data)


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
            await update_social(str(interaction.user.id), "insta", str(modal.updated.value))
        elif select.values[0] == "snap":
            await update_social(str(interaction.user.id), "snapchat", str(modal.updated.value))
        elif select.values[0] == "spotify":
            await update_social(str(interaction.user.id), "spotify", str(modal.updated.value))
        elif select.values[0] == "snaplink":
            await update_social(str(interaction.user.id), "snaplink", str(modal.updated.value))
        elif select.values[0] == "github":
            await update_social(str(interaction.user.id), "github", str(modal.updated.value))

        select.disabled = True
        await interaction.message.edit(view=self)
