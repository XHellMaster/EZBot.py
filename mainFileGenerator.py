mainPy = """"""


def generate(token: str, app_id: str, guild_id: str):
    global mainPy
    mainPy += f"""
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
