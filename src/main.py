import asyncio
import logging
import signal

import discord
from discord.ext.commands import Bot

from basic_project_logger import setup_logging

from cogs.bot_control import SyncCog
from cogs.dictionary.main import DalDictionaryCog
from cogs.logger import LoggingCog
from cogs.tests_for_logger import (
    LoggingTestOneCog, LoggingTestTwoCog, LoggingTestThreeCog
)
from settings import bot_settings


setup_logging()


async def main():
    app_logger = logging.getLogger("app")

    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True

    my_bot = Bot(
        command_prefix="!",
        intents=intents,
        status=discord.Status.idle,
        activity=discord.Game(name="Eternal procrastination"),
    )

    my_bot.on_ready = lambda: app_logger.info(f"Logged in as {my_bot.user} (ID: {my_bot.user.id})")

    app_logger.info("Loading the cogs...")
    await my_bot.add_cog(
        LoggingCog(bot=my_bot, channel_id=bot_settings.logging_channel_id)
    )

    await my_bot.add_cog(LoggingTestOneCog())
    await my_bot.add_cog(LoggingTestTwoCog())
    await my_bot.add_cog(LoggingTestThreeCog())

    await my_bot.add_cog(SyncCog())

    await my_bot.add_cog(DalDictionaryCog())

    try:
        app_logger.info("Starting the bot...")
        await my_bot.start(bot_settings.discord_token)
    except asyncio.CancelledError:
        app_logger.info("Closing the bot...")
        await my_bot.close()
        app_logger.info("Bot was closed gracefully!")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    main_task = asyncio.ensure_future(main())
    loop.add_signal_handler(signal.SIGTERM, main_task.cancel)

    try:
        loop.run_until_complete(main_task)
    finally:
        loop.close()
