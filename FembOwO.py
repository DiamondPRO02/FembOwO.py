import discord
import logging
import json
import datetime
from discord.ext import commands
from discord.utils import get

#json config load
with open('config.json', 'r') as json_config:
    config = json.load(json_config)
json_config.close
#prefix and command
prefix = config.get("prefix")
bot = commands.Bot(command_prefix='!')
#CRITICAL, ERROR, WARNING, INFO and DEBUG
logging.basicConfig(level=logging.INFO)
#file logging
"""
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

@bot.event
async def on_message(message):
    prefix = config.get("prefix")
    if message.author.id == bot.user.id:
        return
"""
@bot.command()
<<<<<<< HEAD
async def ping(ctx):
    await ctx.send(f'Ping: {round(bot.latency * 1000)}ms')
@bot.command()
=======
>>>>>>> edafe054e2d0a639cf5402c0ed25c23371caef6c
async def helping(ctx):
    embed = discord.Embed(
        title = 'Help page',
        description = 'This is the help page (WIP)'
    )
    embed.set_image(url='https://discordemoji.com/assets/emoji/2788_stupid.png')
    embed.set_footer(text='Laget av Alexander Gnauck 3ELDEA')

    await ctx.send(embed = embed)
    pass
@bot.command()
async def hello(ctx):
    await ctx.send('Hello!', mention_author=True)
    print('hello test success!')
<<<<<<< HEAD
@bot.command()
=======
@commands.command()
>>>>>>> edafe054e2d0a639cf5402c0ed25c23371caef6c
async def time(ctx):
    date_time = datetime.datetime.now()
    await ctx.send('The time is:', date_time)
    print('timetelling test success!')
<<<<<<< HEAD
=======
bot.add_command(time)

>>>>>>> edafe054e2d0a639cf5402c0ed25c23371caef6c
#NOT WORKING
@bot.event
async def on_member_join(member):
    guild = member.guild
    print('welcome member #1 test success!')
    if guild.system_channel is not None:
        to_send = 'Welcome {member.mention} to {guild.name}!'
        await guild.system_channel.send(to_send)
        print('welcome member #2 test success!')

#activated when bot ready
@bot.event
async def on_ready():
    start_time = datetime.datetime.now()
    print('We have logged in as {0.user} (ID: {0.user.id}) \nTime:'.format(bot), start_time, '\nPrefix:', prefix)
    print('----------------------------------------------------------------------')
<<<<<<< HEAD
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="ur mum"))
=======
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Frick me"))
>>>>>>> edafe054e2d0a639cf5402c0ed25c23371caef6c

#token
token = config.get("token")
bot.run(token)