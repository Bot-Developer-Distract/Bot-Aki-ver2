from discord.ext import commands
class Ping(commands.Cog):
    config = {
        "name": "ping",
        "desc": "kiểm tra độ trễ của bot",
        "use": "<prefix>ping",
        "author": "King."
    }
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ping(self,ctx):
        await ctx.reply(f"Ping: `{self.bot.latency * 1000 :.2f}` ms")
        await ctx.reply(f"API: `{self.bot.latency * 1000 :.2f}` ms")
        await.ctx.reply(f"Websocket: `{self.bot.latency * 1000 :.2f}` ms")
    


async def setup(bot):
    await bot.add_cog(Ping(bot))