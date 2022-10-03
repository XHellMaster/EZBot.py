cogsPy = """
import discord
from discord import app_commands
from discord.ext import commands

class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        
"""


def add_cog_command(command_name: str, command_desc: str, command_args: str, command_function: str):
    global cogsPy
    cogsPy += f"""
    @app_commands.command(
        name="{command_name}",
        description="{command_desc}"
    )
    async def {command_name}(self,
                     interaction: discord.Interaction"""
    if command_args != "":
        cogsPy += f""",{command_args}"""
    cogsPy += f"""):
        {command_function}"""


def final(guild_id: str):
    global cogsPy
    cogsPy += f"""\n

    async def setup(bot: commands.Bot) -> None:
        await bot.add_cog(
            Commands(bot),
            guilds=[discord.Object(id={guild_id})]
        )
    """


add_cog_command("test", "Sends test", "", """interaction.response.sendMessage(\"Hello!\")""")
add_cog_command("test2", "Sends test twice", "",
                """interaction.response.sendMessage(\"Hello!\")
                interaction.response.sendMessage(\"Hello!\")""")
final("1025517440723079198")

print(cogsPy)
