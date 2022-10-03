import os


class Generator:
    def __init__(self, botname: str, command_groups: list) -> None:
        self.botname = botname
        self.command_groups = command_groups


    def add_command_group(self, command_group: str) -> None:
        self.command_groups.append(command_group)

    cogsPy = """"""

    def create_cog_base(self, command_group: str) -> None:
        if not os.path.exists(os.getcwd()+ f"{self.botname}\\cogs\\{command_group}"):
            cogsPy = """"""
            cogsPy += f"""
import discord
from discord import app_commands
from discord.ext import commands

class {command_group}(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    """
            with open(os.getcwd() + f"\\{self.botname}\\cogs\\{command_group}.py", "w") as cog_file:
                cog_file.write(cogsPy)
                cog_file.close()
            print(f"successfully generated {command_group}.py file at: " + os.getcwd() + f"\\{self.botname}\\cogs\\{command_group}.py")

    def add_cog_command(self, command_group: str, command_name: str, command_desc: str, command_args: list, command_function: str) -> None:
        data = f"""
        
    @app_commands.command(
        name="{command_name}",
        description="{command_desc}"
    )
    async def {command_name}(
        self,
        interaction: discord.Interaction"""
        if bool(command_args):
            for arg in command_args:
                data += f""",  \n\t\t{arg}"""
        data += f"""
    ) -> None:
        {command_function}
"""
        with open(os.getcwd() + f"\\{self.botname}\\cogs\\{command_group}.py", "a") as cog_file:
            cog_file.write(data)
            cog_file.close()
    def close_cog(self, command_group: str, guild_id: str) -> None:
        data = f"""
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        {command_group}(bot),
        guilds=[discord.Object(id={guild_id})]
    )
"""
        with open(os.getcwd() + f"\\{self.botname}\\cogs\\{command_group}.py", "a") as cog_file:
            cog_file.write(data)
            cog_file.close()


    def generateFiles(self, token: str, app_id: str, guild_id: str) -> None:
        name = self.botname
        mainPy = f"""
import discord
from discord.ext import commands

token = \"{token}\"

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            command_prefix=\"/\",
            intents=discord.Intents.all(),
             application_id={app_id}
        )
        self.initial_extensions = [
            "cogs.SampleCommandGroup1",
            "cogs.SampleCommandGroup2",
            "cogs.SampleCommandGroup3"
        ]

    async def onReady(self):
        print(f\"{{self.user}} has connected successfully.\")

    async def setup_hook(self):
        for cog in self.initial_extensions:
            await self.load_extension(cog)
        await bot.tree.sync(guild=discord.Object(id={guild_id}))


bot = Bot()
bot.run(token)
"""

        if not os.path.exists(os.getcwd() + f"\\{name}\\cogs"):
            os.makedirs(os.getcwd() + f"\\{name}\\cogs")
            print("Successfully generated cogs directory at: " + os.getcwd() + f"\\{name}\\cogs")

        if not os.path.exists(os.getcwd() + f"\\{name}\\main.py"):

            with open(os.getcwd() + f"\\{name}\\main.py", "w") as main_file:
                main_file.write(mainPy)
                main_file.close()
            print("successfully generated main.py file at: " + os.getcwd() + f"\\{name}\\main.py")