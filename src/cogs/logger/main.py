import logging

from discord.ext.commands import Cog, Bot

from .filters import CreditCardFilter
from .handlers import DiscordChannelHandler
from .embed_formatter import DiscordEmbedFormatter


class LoggingCog(Cog):
    def __init__(self, bot: Bot, channel_id: int) -> None:
        self.bot = bot
        self.channel_id = channel_id
        self.discord_channel_handler = None
        self.logger = logging.getLogger('app.LoggingCog')

    async def cog_load(self) -> None:
        self.discord_channel_handler = DiscordChannelHandler(
            self.bot, self.channel_id
        )
        self.discord_channel_handler.setFormatter(DiscordEmbedFormatter())
        self.discord_channel_handler.setLevel(logging.WARNING)
        self.discord_channel_handler.addFilter(CreditCardFilter())

        # add Discord logger to existing top level logger `app`
        app_logger = logging.getLogger('app')
        app_logger.addHandler(self.discord_channel_handler)

        self.logger.info('Loaded')

    async def cog_unload(self) -> None:
        logging.getLogger('app').removeHandler(self.discord_channel_handler)

        self.logger.info('Unloaded')
