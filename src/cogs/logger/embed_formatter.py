import logging
from datetime import datetime

import discord
from discord import Embed


class NoParsingFilter(logging.Filter):
    def filter(self, record):
        return not record.getMessage().startswith('parsing')


CRITICAL_THUMBNAIL = "https://cdn.discordapp.com/attachments/1220280725841117204/1220281056037572618/image_processing20200309-6787-1t1kpk5.png?ex=660e5e4b&is=65fbe94b&hm=28b1e0022620ed4aa2ac931f46609d8868a0a466733b8d39841946290e926709&"

COLOR = {
    logging.CRITICAL: discord.Color.from_rgb(198, 252, 3),
    logging.ERROR: discord.Color.from_rgb(252, 3, 3),
    logging.WARNING: discord.Color.from_rgb(252, 94, 3),
    logging.INFO: discord.Color.from_rgb(3, 119, 252),
    logging.DEBUG: discord.Color.from_rgb(101, 118, 120),
    logging.NOTSET: discord.Color.from_rgb(101, 118, 120),
}


class DiscordEmbedFormatter(logging.Formatter):
    def format(self, record) -> Embed:
        embed = Embed(
            title=f"{record.levelname} | {record.name}",
            description=record.getMessage(),
            timestamp=datetime.utcnow(),
            color=COLOR[record.levelno]
        )

        if record.levelno == logging.CRITICAL:
            embed.set_thumbnail(url=CRITICAL_THUMBNAIL)

        if record.exc_info:
            index = min(record.exc_text.find("\n\n"), 1023)
            embed.add_field(name="Traceback", value=f"{record.exc_text[:index]}", inline=False)

        return embed

