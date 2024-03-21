import asyncio
import logging

import aiohttp
from discord import Webhook, Embed
from discord.ext.commands import Bot


class DiscordChannelHandler(logging.Handler):
    def __init__(self, bot: Bot, channel_id: int) -> None:
        super().__init__()
        self.channel_id = channel_id
        self.bot = bot

    def emit(self, record: logging.LogRecord) -> None:
        asyncio.create_task(self.send_message_to_channel(self.format(record)))
        # Actually need to use more complex approach with second thread and
        # separate loop for collecting log messages and handling exceptions
        # because while bot is closing, some tasks still can be pending which
        # will lead to `Session closed` exception

    async def send_message_to_channel(self, message: str | Embed) -> None:
        # wait until bot is ready, otherwise it will raise an exception
        await self.bot.wait_until_ready()
        channel = self.bot.get_channel(self.channel_id)

        # Our message to Discord handler should be an Embed object because of
        # formatting, but if formatting was not applied, let send it as simple
        # message
        if isinstance(message, Embed):
            await channel.send(embed=message)
        else:
            await channel.send(message)


class DiscordWebhookHandler(logging.Handler):
    def __init__(self, bot: Bot, webhook_url: str) -> None:
        super().__init__()
        self.webhook_url = webhook_url
        self.bot = bot

    def emit(self, record: logging.LogRecord) -> None:
        asyncio.create_task(self.send_webhook(self.format(record)))

    async def send_webhook(self, message: str) -> None:
        await self.bot.wait_until_ready()
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(self.webhook_url, session=session)
            await webhook.send(message)
