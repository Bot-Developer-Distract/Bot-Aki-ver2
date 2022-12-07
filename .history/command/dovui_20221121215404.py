import discord
import aiohttp
from discord.ext import commands
import json
class Dovui(commands.Cog):
    config = {
        "name": "dovui",
        "desc": "Đố vui, ko vui thì thôi:)",
        "use": "<prefix>dovui",
        "author": "John Week  ♌#8686(Dev GL)"
    }
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def dovui(self, ctx):
        try:
            async with aiohttp.ClientSession() as session:
                get = await session.get('https://api.phamvandien.xyz/game/dovui')
                data_txt = await get.text()
                data_json = json.loads(data_txt)
                data = {}
                question = data_json['data']['question']
                option = data_json['data']['option']
                correct = data_json['data']['correct'] 
                msg = f'_*Đây là câu hỏi của bạn:*_ {question}'
                stt = 1
                for i in option:
                    msg += f'\n{stt}.{i}'
                    data[str(stt)] = i
                    stt += 1
                msg += '\nReply tin nhắn theo số thứ tự các đáp án để trả lời'
                send = await ctx.send(msg)
                def check(m):
                    return m.author.id == ctx.author.id and m.channel == ctx.channel and m.reference is not None and m.reference.message_id == send.id
                message = await self.bot.wait_for('message', check=check)
                try:
                    if data[str(message.content)] == correct:
                        await ctx.send(f'Bạn đã trả lời đúng, đáp án là **{correct}**')
                    else:
                        await ctx.send(f'Sai rồi, đáp án là **{correct}**')
                except Exception as e:
                    print(e)
                    await ctx.send(f'Chỉ được trả lời theo số thứ tự các đáp án')
        except Exception as e:
            print(e)
            await ctx.send(f"Lệnh bạn đang sử dụng đã xảy ra lỗi, hãy báo cáo về admin bằng lệnh {get_prefix()[str(ctx.message.guild.id)]['prefix']}callad, hoặc câu trả lời của bạn không phải là một con số")
async def setup(bot):
    await bot.add_cog(Dovui(bot))
