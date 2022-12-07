from time import sleep
import discord
from discord.ext import commands
import aiohttp
from command.random_list import list_color
import random
import json
class Video(commands.Cog):
    config = {
        "name": "video",
        "desc": "lệnh giúp bạn có thể xem video online ngay trên discord",
        "use": "<prefix>video <mã truyện> <chapter số>",
        "author": "John Week(maku team)"
    }
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def video(self,ctx,comicHref:str,chapter:str):
        author_dms = await ctx.author.create_dm()
        params = {
            "comicHref":comicHref,
            "chapter":chapter,
            "apikey":"ntkhang"
        }
        async with self.bot.session.get(f'https://sandbox.api.video/auth/api-key',params=params) as get_answer:
            answer = await get_answer.json()
            for x in answer["data"]:
                await author_dms.send(x)
                sleep(2)

    @commands.command()
    async def tim_truyen(self,ctx,*,content:str):
        dem=1
        author_dms = await ctx.author.create_dm()
        params = {
        "q":content,
        "apikey":"ntkhang"
        }
        async with aiohttp.ClientSession() as session:
            async with session.get('https://sandbox.api.video/auth/api-key',params=params) as get_answer:
                answer = await get_answer.json()
                for x in answer["data"]:
                    await author_dms.send(f"{dem}. **name**:{x['name']}    \n**mã truyện**:{x['href']}")
                    await author_dms.send(f"{x['thumbnail']}")
                    dem=dem+1
                    sleep(2)

async def setup(bot):
    await bot.add_cog(Nettruyen(bot))
