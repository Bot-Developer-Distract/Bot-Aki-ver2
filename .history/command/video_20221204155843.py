import discord
from discord.ext import commands
import aiohttp
import random
class Video(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def cadao(self, ctx):
        config = {
            "name": "video",
            "desc": "Video Việt Nam;)",
            "use": "<prefix>video",
            "author": "Anh Duc(aki team)"
        }
        try:
            async with aiohttp.ClientSession() as session:
                list = await session.get("https://sandbox.api.video/videos")
                list = await list.text()
                list = list.split("**")
                result = random.choice(list)
                await ctx.send(result)
        except Exception as e:
            print(e)
async def setup(bot):
    await bot.add_cog(Video(bot))
