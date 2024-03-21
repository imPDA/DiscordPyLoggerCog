import logging

from discord import Interaction, app_commands
from discord.ext.commands import GroupCog

from settings import bot_settings


@app_commands.guilds(bot_settings.test_server_id)  # make synchronization faster
class LoggingTestOneCog(GroupCog, name="test"):
    def __init__(self) -> None:
        self.logger = logging.getLogger('app.LoggingTestOneCog')

    async def cog_load(self) -> None:
        self.logger.info('Loaded')

    @app_commands.command(description="Send DEBUG level message")
    async def debug(self, interaction: Interaction, message: str = ""):
        self.logger.debug(message)
        await interaction.response.send_message(f"Done", ephemeral=True)

    @app_commands.command(description="Send INFO level message")
    async def info(self, interaction: Interaction, message: str = ""):
        self.logger.info(message)
        await interaction.response.send_message(f"Done", ephemeral=True)

    @app_commands.command(description="Send WARNING level message")
    async def warning(self, interaction: Interaction, message: str = ""):
        self.logger.warning(message)
        await interaction.response.send_message(f"Done", ephemeral=True)

    @app_commands.command(description="Send ERROR level message")
    async def error(self, interaction: Interaction, message: str = ""):
        self.logger.error(message)
        await interaction.response.send_message(f"Done", ephemeral=True)

    @app_commands.command(description="Send CRITICAL level message")
    async def critical(self, interaction: Interaction, message: str = ""):
        self.logger.critical(message)
        await interaction.response.send_message(f"Done", ephemeral=True)
