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
        async def video(self, ctx, arg1 = None):
            if arg1 == None:
                await ctx.send('hãy nhập category')
            else:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'https://sandbox.api.video/videos/?category={arg1}') as resp:
                        data_json = json.loads(await resp.text())
                url = data_json['url']
                em = discord.Embed(colour = random.choice(list_color), description = f'video {arg1}')
                em.set_image(url = url)
                await ctx.send(embed = em)
async def setup(bot):
    await bot.add_cog(video(bot))

