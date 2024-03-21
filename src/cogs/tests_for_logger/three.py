import logging

from discord import Interaction, app_commands
from discord.ext.commands import Cog

from settings import bot_settings


@app_commands.guilds(bot_settings.test_server_id)  # make synchronization faster
class LoggingTestThreeCog(Cog):
    def __init__(self) -> None:
        self.logger = logging.getLogger('app.LoggingTestThreeCog')

    async def cog_load(self) -> None:
        self.logger.info('Loaded')

    @app_commands.command(description="Send CRITICAL with traceback")
    @app_commands.guilds(bot_settings.test_server_id)
    async def raise_exception(self, interaction: Interaction):
        1 / 0

    @raise_exception.error
    async def raise_exception_error(self, interaction: Interaction, exception):
        await interaction.response.send_message("Error occurred", ephemeral=True)

        self.logger.exception("Exception was caught")
        # stacktrace will be added automatically
