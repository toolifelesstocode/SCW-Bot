from disnake import CommandInteraction, Embed, Interaction
from disnake.ext import commands
from utils.Bot import Bot
from utils.config import Faqs, Rules

class Commands(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    role_choice = commands.option_enum({ 
        "News": "966229347637817404", 
        "Updates": "965169353253351454", 
        "He/Him": "966274532241457162", 
        "She/Her": "966274560662052874", 
        "They/Them": "966274561110863872" 
    })

    @commands.slash_command(name="role")
    async def role(self, inter: CommandInteraction, role: role_choice):
        """
        Get a role.

        Parameters
        ----------
        role: The role you want to have.
        """
        roles = inter.guild.get_role(int(role))
        if roles in inter.user.roles:
            await inter.send("Removed the {role.mention} role from you.".format(role=roles), ephemeral=True)
            await inter.user.remove_roles(roles, reason="Removing role.")
        else:
            await inter.send("Added the {role.mention} role to you.".format(role=roles), ephemeral=True)
            await inter.user.add_roles(roles, reason="Adding role.")

    @commands.slash_command(name="faq")
    async def faq(self, inter: CommandInteraction, question: str):
        """
        Get an answer to your question.

        Parameters
        ----------
        question: Your question.
        """
        if question in Faqs.keys():
            faq_embed = Embed(color=2795310, description=Faqs[question], title=question)
            await inter.response.defer()
            await inter.edit_original_message(embed=faq_embed)


    @faq.autocomplete("question")
    async def faq_answer(self, inter: CommandInteraction, string: str):
        return [key for key in Faqs.keys() if key.startswith(string)]

    @commands.slash_command(name="rule")
    async def rules(self, inter: CommandInteraction, number: str):
        """
        Get a rule.

        Parameters
        ----------
        number: The number of the rule you want to get.
        """
        if number in Rules.keys():
            rule_embed = Embed(color=2795310, description=Rules[number], title=number)
            await inter.response.defer()
            await inter.edit_original_message(embed=rule_embed)

    @rules.autocomplete("number")
    async def rule_autcomp(self, inter: CommandInteraction, integer: str):
        return [key for key in Rules.keys() if key.startswith(integer)]

def setup(bot: Bot):
    bot.add_cog(Commands(bot))