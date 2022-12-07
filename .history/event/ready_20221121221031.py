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
    Setting `Playing ` status
await bot.change_presence(activity=discord.Game(name="a game"))

# Setting `Streaming ` status
await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

# Setting `Listening ` status
await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

# Setting `Watching ` status
await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))