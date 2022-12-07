import discord
from discord.ext import commands
import aiohttp
import json
import random
from command.random_list import list_color
class video(commands.Cog):
    config = {
      "name": "Video",
      "desc": "gif video theo từng category+)",
      "use": "<prefix>video <category>",
      "author": "Anh Duc(aki team)"
    }
    def __init__(self, bot):
        self.bot = bot
        @commands.command()
                

