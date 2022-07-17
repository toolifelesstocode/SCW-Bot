from logging import getLogger
from traceback import format_exception

from disnake import Colour, CommandInter, Embed
from disnake.ext.commands import Cog
from tempest import Tempest

log = getLogger(__name__)

error_message = """
An error occurred while executing this command.
Please report it to the server owner.

```py
{error}
```
"""


class Listeners(Cog):
    def __init__(self, bot: Tempest):
        self.bot = bot

    @Cog.listener("on_ready")
    async def when_ready(self):
        log.info(f"{self.bot.user} is alive!")

    @Cog.listener("on_slash_command_error")
    async def slash_error(self, itr: CommandInter, error: Exception):
        log.error(f"Error with slash command {itr.application_command.qualified_name}: {error}")
        await itr.send(
            embed=Embed(
                colour=Colour.red(),
                description=error_message.format(
                    error="".join(e for e in format_exception(type(error), error, error.__traceback__))
                ),
            ),
            ephemeral=True
        )
        return


def setup(bot: Tempest):
    bot.add_cog(Listeners(bot))
