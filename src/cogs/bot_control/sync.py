import logging

from discord.ext.commands import Cog, Context, command, is_owner


class SyncCog(Cog):
    def __init__(self) -> None:
        self.logger = logging.getLogger("app.SyncCog")

    async def cog_load(self) -> None:
        self.logger.info("Loaded")

    @command()
    @is_owner()
    async def sync(self, ctx: Context) -> None:
        fmt = await ctx.bot.tree.sync()
        await ctx.send(f"Totally synced {len(fmt)} commands globally")
        if fmt:
            await ctx.send(
                "\n".join([app_command.name for app_command in fmt])
            )

    @command(name="synchere")
    @is_owner()
    async def sync_here(self, ctx: Context) -> None:
        fmt = await ctx.bot.tree.sync(guild=ctx.guild)
        await ctx.send(f"Totally synced {len(fmt)} commands in {ctx.guild}")
        if fmt:
            await ctx.send(
                "\n".join([app_command.name for app_command in fmt])
            )
