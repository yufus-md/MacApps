import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import cogs

load_dotenv()


class bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=discord.Intents.all(),
            activity=discord.Activity(type=discord.ActivityType.playing, name='run /ticket to contact mods')
        )
    
    async def setup_hook(self):
        await self.load_extension("cogs.moderation")
        await self.load_extension("cogs.bot")

bot = bot()
bot.run(os.getenv('TOKEN'))