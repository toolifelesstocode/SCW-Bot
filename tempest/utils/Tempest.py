from os import environ

from disnake import Activity, ActivityType, AllowedMentions
from disnake.ext.commands import InteractionBot
from dotenv import load_dotenv

load_dotenv()


class Tempest(InteractionBot):
    def __init__(self):
        self.config = environ
        super().__init__(
            activity=Activity(name="Sham's Code Workspace", type=ActivityType.watching),
            sync_commands=True,
            sync_commands_on_cog_unload=True,
            allowed_mentions=AllowedMentions(
                everyone=False, users=True, roles=False, replied_user=True
            ),
            owner_id=self.config.get("OWNER_ID"),
        )
