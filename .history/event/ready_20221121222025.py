from distutils.util import change_root
from discord.ext import commands
from discord import *
import io,aiohttp,time,random,datetime
import json
class Welcome(commands.Cog):
    config = {
        "name": "set_welcome",
        "desc": "Tự động chào đón người dùng mới",
        "use": "tự động trả lời khi nhắn tin ở kênh đã cài đặt",
        "author": "King.(maku team)",
        "event": False
    }
   game = discord.Game("with the API")
await client.change_presence(status=discord.Status.idle, activity=game)