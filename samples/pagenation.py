from __future__ import annotations
from discord.ext.ui import View, ViewTracker, Message, PaginationView, MessageProvider
import discord
import os


client = discord.Client()


class Page(View):
    def __init__(self, content: str):
        super(Page, self).__init__()
        self.content = content

    async def body(self) -> Message | View:
        return Message(self.content)


@client.event
async def on_message(message: discord.Message):
    if message.content != "!test":
        return

    view = PaginationView([
        Page("The first page -- Morning --"),
        Page("The second page -- Noon --"),
        Page("The third page -- Afternoon --"),
        Page("The forth page -- Evening --"),
        Page("The last page -- Good night! --"),
    ])
    tracker = ViewTracker(view, timeout=None)
    await tracker.track(MessageProvider(message.channel))


client.run(os.environ["DISCORD_BOT_TOKEN"])