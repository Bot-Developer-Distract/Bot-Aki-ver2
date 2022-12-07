from tkinter import BOTH
import discord
from discord.ext import commands
import aiohttp
import json
import random
from command.random_list import list_color
class Video(commands.Cog):
    config = {
      "name": "Music",
      "desc": "gif video theo từng url +))",
      "use": "<prefix>music ",
      "author": "Anh Duc(aki team)"
    }
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def music(self, ctx, url = None):
        try:
            if url == None:
                await ctx.send("bạn chưa nhập url")
                return
            async with aiohttp.ClientSession() as session:
                get = await session.get(f"https://nekos.best/api/v2/{url}?amount=1")
                data = await get.json()
                if get.status == 200:
                    gif = data["results"][0]["url"]
                    em_load = discord.Embed(colour = random.choice(list_color))
                    em_load.set_image(url = gif)
                    await ctx.reply(embed = em_load)
                    return
                await ctx.send("error")
        except Exception as e:
            print(e)
async def setup(bot):
    await bot.add_cog(Music(bot))

