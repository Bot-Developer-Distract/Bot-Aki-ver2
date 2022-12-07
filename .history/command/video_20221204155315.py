import discord
from discord.ext import commands
import aiohttp
import random
class Video(commands.Cog):
    config = {
        "name": "totinh",
        "desc": "tỏ tình người bạn thích",
        "use": "<prefix>totinh <id người bạn thích> <lời tỏ tình>",
        "author": "King.(maku team)"
    }

    def __init__(self, bot):
    self.bot = bot
  @commands.command()
  async def Video(self, ctx):
    try:
        async with aiohttp.ClientSession() as session:
            get = await session.get(f"https://sandbox.api.video/auth/api-key")
            data = await get.json()
            if get.status == 200:
                gif = data["results"][0]["url"]
                em_load = discord.Embed(colour = random.choice(Video))
                em_load.set_image(url = gif)
                await ctx.reply(embed = em_load)
                return
            await ctx.send("error")
    except Exception as e:
      print(e)
async def setup(bot):
  await bot.add_cog(Video(bot))
