import os


class CogGenerator:
    def __init__(self) -> None:
        pass

    def setupPaths(self, name: str) -> None:

        if not os.path.exists(os.getcwd() + f"\\{name}\\cogs"):
            os.makedirs(os.getcwd() + f"\\{name}\\cogs")

            print("Successfully generated cogs directory at: " + os.getcwd() + f"\\{name}\\cogs")
    cogsPy = """
    import discord
    from discord import app_commands
    from discord.ext import commands

    class Commands(commands.Cog):
        def __init__(self, bot: commands.Bot) -> None:
            self.bot = bot

    """

    def add_cog_command(self, command_name: str, command_desc: str, command_args: str, command_function: str) -> None:
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

    def final(self, guild_id: str) -> None:
        global cogsPy
        cogsPy += f"""\n

        async def setup(bot: commands.Bot) -> None:
            await bot.add_cog(
                Commands(bot),
                guilds=[discord.Object(id={guild_id})]
            )
        """

class MainFilesGenerator:
    def __init__(self) -> None:
        pass


    def generate(token: str, app_id: str, guild_id: str) -> str:
        mainPy = f"""
import discord
from discord.ext import commands


token = \"{token}\"

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            command_prefix=\"$\",
            intents=discord.Intents.all(),
            application_id={app_id}
        )

    async def onReady(self):
        print(f\"{{self.user}} has connected successfully.\")

    async def setup_hook(self):
        await self.load_extension(f\"cogs.Commands\")
        await bot.tree.sync(guild=discord.Object(id={guild_id}))


bot = Bot()
bot.run(token)
"""
        return mainPy
    def setupPaths(self, name: str) -> None:

        if not os.path.exists(os.getcwd() + f"\\{name}\\main.py"):

            with open(os.getcwd() + f"\\{name}\\main.py", "w") as main_file:
                main_file.write(MainFilesGenerator.generate("sample_token", "sample app id", "sample guild id"))
                main_file.close()
            print("successfully generated main.py file at: " + os.getcwd() + f"\\{name}\\main.py")


# add_cog_command("test", "Sends test", "", """interaction.response.sendMessage(\"Hello!\")""")
# add_cog_command("test2", "Sends test twice", "",
#                """interaction.response.sendMessage(\"Hello!\")
#                interaction.response.sendMessage(\"Hello!\")""")
# final("1025517440723079198")