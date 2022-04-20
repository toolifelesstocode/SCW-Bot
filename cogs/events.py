from disnake import Activity, ActivityType
from disnake.ext import commands
from utils.Bot import Bot

class Events(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener("on_ready")
    async def when_turned_on(self):
        print(f"{self.bot.user} is ready!")
        await self.bot.change_presence(activity=Activity(name="Sham's Code Workspace", type=ActivityType.watching))

def setup(bot: Bot):
    bot.add_cog(Events(bot))