import logging

from discord import app_commands, Interaction
from discord.ext import tasks
from discord.ext.commands import Cog

from settings import bot_settings


class LoggingTestTwoCog(Cog):
    def __init__(self) -> None:
        self.logger = logging.getLogger('app.LoggingTestTwoCog')
        self.level = 0

    async def cog_load(self) -> None:
        self.logger.info('Loaded')

    async def cog_unload(self) -> None:
        self.periodical_log.cancel()

    @tasks.loop(seconds=10)
    async def periodical_log(self):
        self.logger.log(self.level, "Some %s level message", logging.getLevelName(self.level))

        # first message will be ignored by both Stream and Discord handlers (NOTSET level)
        # Stream handler will catch all messages starting from DEBUG
        # Discord handler will catch only messages starting from WARNING

        self.level += 10

        if self.level >= 60:
            self.periodical_log.cancel()

    @app_commands.command(description="Send test messages of all levels")
    @app_commands.guilds(bot_settings.test_server_id)
    async def test_all_levels(self, interaction: Interaction):
        if self.periodical_log.is_running():
            return await interaction.response.send_message(
                "This test still running, try again later", ephemeral=True
            )

        self.periodical_log.start()
        await interaction.response.send_message("Done", ephemeral=True)
