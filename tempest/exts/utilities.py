from disnake import Colour, CommandInter, Embed, utils
from disnake.ext.commands import Cog, option_enum, slash_command
from tempest import Tempest
from tempest.utils.dicts import FAQS, RULES

role_choice = option_enum(
    {
        "News": "966229347637817404",
        "Updates": "965169353253351454",
        "He/Him": "966274532241457162",
        "She/Her": "966274560662052874",
        "They/Them": "966274561110863872",
    }
)


class Utilities(Cog):
    def __init__(self, bot: Tempest):
        self.bot = bot

    @slash_command()
    async def roles(self, itr: CommandInter, role: role_choice):
        """Get roles of your choice.

        Parameters
        ----------
        role: The role(s) you want to get.
        """
        roles = itr.guild.get_role(int(role)) or utils.get(
            itr.guild.roles, id=int(role)
        )
        if roles in itr.user.roles:
            await itr.user.remove_roles(roles, reason="Removed role from user")
            await itr.response.send_message(f"Removed {roles.name} from you.")
            return
        else:
            await itr.user.add_roles(roles, reason="Added role to user")
            await itr.response.send_message(f"Added {roles.name} to you.")

    @slash_command()
    async def faq(self, itr: CommandInter, question: str):
        """Get a possible answer to your question."""
        if question in FAQS:
            faq_embed = Embed(
                title=question, description=FAQS[question], colour=Colour.purple()
            )
            await itr.response.send_message(embed=faq_embed)
        else:
            await itr.response.send_message(
                f"No answer found for `{question}`.", ephemeral=True
            )

    @faq.autocomplete(option_name="question")
    async def question_autocomplete(self, itr: CommandInter, question: str):
        """Your question."""
        return [q for q in FAQS if q.startswith(question)]

    @slash_command()
    async def rules(self, itr: CommandInter, number: str):
        """Get a rule by number."""
        if number in RULES:
            rule_embed = Embed(
                title=f"Rule {number}",
                description=RULES[number],
                colour=Colour.purple(),
            )
            await itr.response.send_message(embed=rule_embed)
        else:
            await itr.response.send_message(
                f"No rule found for `{number}`.", ephemeral=True
            )

    @rules.autocomplete(option_name="number")
    async def number_autocomplete(self, itr: CommandInter, number: str):
        """Your number."""
        return [n for n in RULES if n.startswith(number)]


def setup(bot: Tempest):
    bot.add_cog(Utilities(bot))
