import discord
from discord.ext import commands
import aiohttp
import json
import random
from command.random_list import list_color
class Video(commands.Cog):
    config = {
      "name": "Video",
      "desc": "gif video theo từng category+)",
      "use": "<prefix>video <category>",
      "author": "Anh Duc(aki team)"
    }
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def Video(self, ctx):
        try:
            async with aiohttp.ClientSession() as session:
                get = await session.get('https://api.tenor.com/v1/categories?key=5I5ZCZV7OZQH')
                data = await get.json()
                categories = data['categories']
                category = random.choice(categories)
                await ctx.send(f'Category: {category}')
                get = await session.get(f'https://api.tenor.com/v1/random?key=5I5ZCZV7OZQH&q={category}&limit=1')
async def setup(bot):
  await bot.add_cog(Video(bot))

