from discord.ext import commands
import discord


class Thongtin(commands.Cog):
    config = {
        "name": "thongtin",
        "desc": "kiểm tra thời gian online của bot",
        "use": "<prefix>thongtin",
        "author": "81CuognVn"
    }

    def __init__(self, bot):
        self.bot = bot
    

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@commands.command()
async def on_message(message):
    if message.content.startswith("_userinfo"):
        emb14 = discord.Embed(
            title=f"@{message.author} info:",
            colour=discord.Colour.dark_blue()
        )
        emb14.set_image(url=message.author.avatar_url)
        emb14.add_field(name=f"Name", value=f"{message.author}", inline=True)
        emb14.add_field(name=f"Discord Joined date", value=f"{message.author.created_at}", inline=True)
        emb14.add_field(name=f"Server Joined date", value=f"{message.author.joined_at}", inline=True)
        await message.channel.send(embed=emb14)
async def setup(bot):
    await bot.add_cog(Thongtin(bot))

