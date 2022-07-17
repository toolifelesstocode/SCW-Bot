from logging import INFO, basicConfig, getLogger

from tempest import Tempest

bot = Tempest()
log = getLogger(__name__)
basicConfig(
    level=INFO,
    datefmt="%Y-%m-%d - %H:%M:%S",
    format="[%(asctime)s] | %(name)s | %(levelname)s | %(message)s",
)


def start():
    try:
        bot.load_extensions("tempest/exts")
    except Exception as err:
        log.error(f"Error loading extensions: {err}")
    bot.run(bot.config.get("TOKEN"))


if __name__ == "__main__":
    start()
