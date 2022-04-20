from disnake import Intents
from disnake.ext import commands

class Bot(commands.InteractionBot):
    def __init__(self):
        super().__init__(sync_commands=True, 
            sync_commands_on_cog_unload=True, 
            sync_permissions=True, 
            test_guilds=[949717907942830140],
            intents=Intents(guilds=True, members=True))