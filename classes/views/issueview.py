import aiohttp
import discord
from discord.ui import View
from discord import SelectOption
from classes.modals.issuemodal import PostIssue
from config import settings


class IssueReq:
    async def postIssue(title, body, user, label):
        headers = {"Authorization": f"token {settings.GITTOKEN}", "Accept": "application/vnd.github.v3+json"}
        data = {"title": title, "body": body + f"\n\n\n**Issued by:** {user}", "labels": [f"{label}"]}
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"https://api.github.com/repos/chinouvm/esie-bot/issues",
                headers=headers,
                json=data,
            ):
                pass


class PostIssueView(View):
    @discord.ui.select(options=[SelectOption(label="Report a bug", value="Bug"), SelectOption(label="Make a suggestion", value="Suggestion")])
    async def select_callback(self, interaction, select):
        modal = PostIssue()
        await interaction.response.send_modal(modal)
        await modal.wait()
        await IssueReq.postIssue(modal.issuetitle.value, modal.issuebody.value, interaction.user, select.values[0])
        select.disabled = True
        await interaction.message.edit(view=self)
