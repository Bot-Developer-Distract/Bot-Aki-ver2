import discord
from discord.ext import commands
import aiohttp
import json
import random
from command.random_list import list_color
class Video(commands.Cog):
    def __init__(self, bot):
    self.bot = bot
  @commands.command()
  async def video(self, ctx, category = None):
    try:
        if category== None:
            await ctx.send("bạn chưa nhập category")
            return
        async with aiohttp.ClientSession() as session:
            get = await session.get(f"https://sandbox.api.video/videos")
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
  await bot.add_cog(Video(bot))

