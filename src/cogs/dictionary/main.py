import logging
import pathlib
import re

from discord import app_commands, Interaction
from discord.ext.commands import Cog, Bot

from cogs.dictionary.dal_dictionary import read_dictionary
from settings import bot_settings


class DalDictionaryCog(Cog):
    def __init__(self) -> None:
        self.logger = logging.getLogger('app.DalDictionaryCog')
        self.dictionary = read_dictionary(pathlib.Path(__file__).resolve().parent / "Dal.txt")

    async def cog_load(self) -> None:
        self.logger.info('Loaded')

    @app_commands.command(description="Найти слово в толковом словаре Даля")
    @app_commands.guilds(bot_settings.test_server_id)
    async def dal(self, interaction: Interaction, word: str):
        word = word.upper()

        self.logger.info(
            "<%s> (%d) searching for word <%s> in guild <%s> (%d)",
            interaction.user.global_name,
            interaction.user.id,
            word,
            interaction.guild.name,
            interaction.guild.id
        )

        if len(re.sub(r"[^А-Я-]", " ", word)) < len(word):
            return await interaction.response.send_message(
                f'Слово может содержать только кириллицу и дефис', ephemeral=True
            )

        definition = self.dictionary[word[0]].get(word)
        if not definition:
            return await interaction.response.send_message(
                f'Определение `{word}` не найдено в толковом словаре Даля', ephemeral=True
            )
        # TODO: try to find a closest match
        # TODO: beatify output with Embed

        await interaction.response.send_message(
            f'Определение слова `{word}` в толковом словаре Даля:\n> {definition}'
        )

    @dal.autocomplete("word")
    async def dal_word_autocomplete(
            self, interaction: Interaction, current: str
    ) -> list[app_commands.Choice[str]]:
        if not current:
            return []

        current = current.upper()
        words = self.dictionary[current[0]]
        return [
            app_commands.Choice(name=word, value=word) for word in words
            if word.startswith(current)
        ][:25]
