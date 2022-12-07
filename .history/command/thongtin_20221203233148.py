from discord.ext import commands
import discord


class Uptime(commands.Cog):
    config = {
        "name": "uptime",
        "desc": "kiểm tra thời gian online của bot",
        "use": "<prefix>uptime",
        "author": "81CuognVn"
    }

    def __init__(self, bot):
        self.bot = bot

        self.START_TIME = None