from discord.ui import View
import discord


class MarryView(View):
    @discord.ui.button(label="Yes", style=discord.ButtonStyle.green, custom_id="yes")
    async def buttonupvote_callback(self, interaction, button):
        button.disabled = True
        button.label = "Validating..."
        buttonNo = [x for x in self.children if x.custom_id == "no"][0]
        buttonNo.disabled = True
        await interaction.response.edit_message(view=self)

    @discord.ui.button(label="No", style=discord.ButtonStyle.red, custom_id="no")
    async def buttondownvote_callback(self, interaction, button):
        button.disabled = True
        button.label = "Validating..."
        buttonYes = [x for x in self.children if x.custom_id == "yes"][0]
        buttonYes.disabled = True
        await interaction.response.edit_message(view=self)
