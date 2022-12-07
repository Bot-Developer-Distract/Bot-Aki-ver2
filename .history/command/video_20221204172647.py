from tkinter import BOTH
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
    async def video(self, ctx, arg1 = None):
        if arg1 == None:
            await ctx.send('hãy nhập category')
        else:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api.hclaptrinh.repl.co/api/video/{arg1}') as resp:
                    data_json = json.loads(await resp.text())
            if data_json['status'] == 'error':
                await ctx.send('category không tồn tại')
            else:
                em = discord.Embed(colour = random.choice(list_color), description = f'category: {arg1}')
                em.set_image(url = data_json['url'])
                await ctx.send(embed = em)
async def setup(bot):
    await bot.add_cog(Video(bot))


