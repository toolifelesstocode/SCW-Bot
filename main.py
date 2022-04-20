import os
from utils.Bot import Bot
from utils.config import Token

bot = Bot()

for fn in os.listdir("cogs"):
    if fn.endswith(".py") and not fn.startswith("_"):
        name = fn[:-3]
        bot.load_extension(f"cogs.{name}")

try:
    bot.run(Token)
except Exception as e:
    print("Error while logging in: {0}".format(e))