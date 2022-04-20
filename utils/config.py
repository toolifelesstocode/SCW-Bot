import os
from dotenv import load_dotenv
load_dotenv()

Token: str = os.environ.get("TOKEN")
Faqs: dict[str, str] = {
    "How do I get roles?": "You can get roles by using the `/role` command, and selecting the role you want.",
    "How do I get the videos' source code?": "That's the neat part. You don't :p",
    "How do I become a moderator?": "You will have to wait for the staff applications to open. However you need to be active.",
    "Why is my name now Moderated Nickname?": "Your user-name was possibly un-pingable or was using the Zalgo font, which also isn't pingable."
}

Rules = {
    "Rule 1": "Do not be a discriminatory to anyone — Such as, being racist, homophobic, transphobic, misogynistic, etc. — We want everyone to live how they want to live.",
    "Rule 2": "Do not spam in any channel.",
    "Rule 3": "Do not send anything that will flood channels — This applies for support channels too.",
    "Rule 4": "Do not send any NSFW or NSFL — Some people here are young and we want every user to be safe and protected from such stuff.",
    "Rule 5": "Abide by [Discord's ToS](https://discord.com/terms)",
    "Rule 6": "Do not DM people without their permission — Some people aren't comfortable DM'ing random people on the internet.",
    "Rule 7": "Keep the channels with a good vibe. We all want to just enjoy life.",
    "Rule 8": "Do not advertise, this includes DM-advertising.",
    "Rule 9": "Keep help questions in support channels — We want to keep the channels as clean as possible.",
    "Rule 10": "Do not use any 3rd-Party Discord clients to harm anyone or the server — You can use BetterDiscord, Powercord, etc, sure, but if you use stuff like message logging, you will be kicked/banned until further notice."
}