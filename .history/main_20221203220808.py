from discord.ext.commands import *
from discord.ext import commands, tasks
import discord 
from discord import *
import aiohttp
import sqlite3
import os
import time
import nest_asyncio
import asyncio
import json
import requests
import itertools


from host.webdriver import server

# khai báo
# =============================================#
nest_asyncio.apply()
with open('config.json', 'r') as f:
    config = json.load(f)
bot = commands.Bot(command_prefix=config['prefix'], intents=Intents.all(), help_command=None)
bot.database = sqlite3.connect('data.db', timeout=10)
bot.sql = bot.database.cursor()
# =============================================#

# treo bot
# =============================================#
on_replit = config.get('on_replit', False)

if on_replit:
    server()

else:
    ...


# =============================================#

# hàm chung
# =============================================#
async def update(user, change, mode):
    if mode == "win_wallet":
        bot.sql.execute(f'UPDATE user_data SET user_money = user_money + {change} WHERE user_id={user}')
    elif mode == "lose_wallet":
        bot.sql.execute(f'UPDATE user_data SET user_money = user_money - {change} WHERE user_id={user}')
    elif mode == "win_bank":
        bot.sql.execute(f'UPDATE user_data SET user_bank = user_bank + {change} WHERE user_id={user}')
    elif mode == "lose_bank":
        bot.sql.execute(f'UPDATE user_data SET user_bank = user_bank - {change} WHERE user_id={user}')


async def open_account(user):
    users = await get_bank_data()
    if str(user) in users:
        return False
    else:
        users[str(user)] = {}
    save_member_data(users)
    return True


async def get_bank_data():
    with open("command/data.json", 'r') as f:
        users = json.load(f)
    return users


def save_member_data(data):
    with open("command/data.json", 'w') as f:
        json.dump(data, f)


# =============================================#


# hàm chính chạy bot
# =============================================#
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.reply(f"Không tìm thấy lệnh `{ctx.invoked_with}`")

    elif isinstance(error, CommandOnCooldown):
        await ctx.reply(f"Xài lệnh chậm thôi bạn ơi. Hãy thử lại sau {error.retry_after :.3f}s")


@bot.event
async def on_ready() -> None:
    status_task.start()

@tasks.loop()
async def status_task() -> None:
    
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game("với electricity(năng lượng tích cực) ⚡"))
    await asyncio.sleep(60)
    await bot.change_presence(activity=discord.Streaming(name="Official Server With Dedication 🥰", url="http://bit.ly/3AZkvoK"))
    await asyncio.sleep(60)
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="commands | Type ?/help for help 💁"))
    await asyncio.sleep(60)
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="tất cả member enjoying my shocks 😳"))
   
    #activity = Game(name="Đang chơi game mà <3", type=3)
    await bot.change_presence(status=Status.online, activity=activity)
    await asyncio.sleep(3)
    game = Game(name ="Hấp dẫn cùng WC ✍️", type=3)
    await bot.change_presence(status=Status.idle, activity=game)
    await asyncio.sleep(3)
    game = Game(name ="Hãy thử xài lệnh help 🪧", type=3)
    await bot.change_presence(status=Status.dnd, activity=game)
    await asyncio.sleep(3)


async def setup_hook():
    bot.session = aiohttp.ClientSession(loop=bot.loop)


setattr(bot, 'setup_hook', setup_hook)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    await bot.process_commands(message)


async def main():
    thong_bao = requests.get(url='https://api-iotran.tk/aki-bot/update').json()
    print(bcolors.WARNING + '                      MODULE' + bcolors.ENDC)
    print('═══════════════════════════════════════════════════')
    dem_lenh = 0
    commands = os.listdir('command')
    for command in commands:
        if (command == '__pycache__' or command == 'random_list' or command == "data.json" or command == "cache"):
            pass
        else:
            try:
                await bot.load_extension(f"command.{command[:-3]}")
                print(bcolors.OKBLUE + f'>> load thành công module {command[:-3]}' + bcolors.ENDC)
                dem_lenh = dem_lenh + 1
                time.sleep(0.025)
            except Exception as e:
                print(bcolors.FAIL + f'>> load thất bại module {command[:-3]} ({e})' + bcolors.ENDC)
    print('═════════════════════════════════════════════════════')
    print(bcolors.WARNING + '                      EVENT' + bcolors.ENDC)
    print('═════════════════════════════════════════════════════')
    for command in os.listdir("./event"):
        if (command == '__pycache__' or command == 'random_list' or command == "data.json"):
            pass
        else:
            await bot.load_extension(f"event.{command[:-3]}")
            print(bcolors.OKBLUE + f'>> load thành công module {command[:-3]}' + bcolors.ENDC)
            time.sleep(0.025)
    print('═════════════════════════════════════════════════════')
    print(bcolors.OKGREEN + '''
 █████╗ ██╗  ██╗██╗    ██████╗  ██████╗ ████████╗
██╔══██╗██║ ██╔╝██║    ██╔══██╗██╔═══██╗╚══██╔══╝
███████║█████╔╝ ██║    ██████╔╝██║   ██║   ██║   
██╔══██║██╔═██╗ ██║    ██╔══██╗██║   ██║   ██║   
██║  ██║██║  ██╗██║    ██████╔╝╚██████╔╝   ██║   
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝    ╚═════╝  ╚═════╝    ╚═╝   
                                                 
                                                                       
''' + bcolors.ENDC)
    print(f'''
        ══╦═════════════════════════════════╦══
╔═════════╩═════════════════════════════════╩═════════╗      
║ TÁC GIẢ:John Week  ♌#8686                 
║ CHỦ SỞ HỮU BOT: {config['admin_name']}({config['admin_id']})                          
║ TÊN BOT:{config['bot_name']}  
║ PREFIX:{config['prefix']}   
║ PHIÊN BẢN:{thong_bao['version']}                       
║ SỐ MODULE(LỆNH) HIỆN CÓ TRONG BOT: {dem_lenh}                   
╚═════════════════════════════════════════════════════╝
''')
    try:
        print(bcolors.WARNING + f">> Khởi động thành công {config['bot_name']} <<" + bcolors.ENDC)
        print(bcolors.OKBLUE + f'''Lời nhắn của aki team :{thong_bao['message']}''' + bcolors.ENDC)

        token = (os.environ if on_replit else config)['token']
        await bot.start(token)

    except Exception as e:
        print(bcolors.WARNING + '>> LỖI TOKEN BOT <<' + bcolors.ENDC)


activities = itertools.cycle([
    Game(name=config["status"], type=3),
    discord.Activity(type=discord.ActivityType.watching, name=f"{bot.command_prefix}help")
])
activities2 = itertools.cycle([
    Game(name=config["status1"], type=3),
    discord.Activity(type=discord.ActivityType.playing, name=f"{bot.command_prefix}help") 
])    



async def check_update():
    user = "iotranvn"
    repo = "aki-bot"
    
    url = "https://api.github.com/repos/{}/{}/git/trees/master?recursive=1".format(user, repo)
    async with aiohttp.ClientSession() as session:
        r = await session.get(url)
        res = await r.json()
        list_command = []
        for file in res["tree"]:
            data = file["path"]
            if "__pycache__" in data:
                pass
            elif "command/" not in data:
                pass
            else:
                list_command.append(data.replace("command/", ""))
                command = os.listdir("./command")
                for i in list_command:
                    if i not in command and i.endswith(".py") and "/" not in i:
                        print(f"Có module mới chưa được update trong file của bạn là: {i}. Đang tiến hành update...")
                        code = await session.get(f"https://raw.githubusercontent.com/iotranvn/aki-bot/master/command/{i}")
                        f = open(f"command/{i}", "w")
                        f.write(await code.text())
                        f.close()
@tasks.loop(seconds=5)
async def task_loop():
    await bot.change_presence(activity=next(activities), status=Status.dnd)


try:
    asyncio.run(check_update())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
except Exception as e:
    print(e)
    os.system("kill 1")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

# =============================================#
       









