import discord
import logging
import json
import datetime
from discord.ext import commands
from discord.utils import get

client = discord.Client()
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

@client.event
async def on_message(message):
    prefix = config.get("prefix")
    if message.author.id == client.user.id:
        return
    if not message.content.startswith(prefix):
        print('prefix fail test success!')
        return
#write if prefix !== message content startwith => return
    if message.content.startswith(prefix + 'hello'):
        await message.channel.send('Hello!', mention_author=True)
        print('hello test success!')
        return
    if message.content.startswith(prefix + 'time'):
        start_time = datetime.datetime.now()
        await message.channel.send('The time is:', start_time)
        print('timetelling test success!')
        return
"""
@bot.command()
async def hello(ctx):
    await ctx.send('Hello!', mention_author=True)
    print('hello test success!')
    pass
@commands.command()
async def time(ctx):
    date_time = datetime.datetime.now()
    await ctx.send('The time is:', date_time)
    print('timetelling test success!')
    pass
bot.add_command(time)
#NOT WORKING
@client.event
async def on_member_join(member):
    guild = member.guild
    print('welcome member #1 test success!')
    if guild.system_channel is not None:
        to_send = 'Welcome {member.mention} to {guild.name}!'
        await guild.system_channel.send(to_send)
        print('welcome member #2 test success!')
#Fuck me
class MyClient(discord.Client):
    async def on_member_join(self, member):
        guild = member.guild
        print('welcome member #11 test success!')
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)
            print('welcome member #22 test success!')
#reeeeeeeeeeeeeeeeeeeeee

@client.event
async def on_ready():
    start_time = datetime.datetime.now()
    print('We have logged in as {0.user} (ID: {0.user.id}) \nTime:'.format(client), start_time, '\nPrefix:', prefix)
    print('----------------------------------------------------------------------')

#token
token = config.get("token")
client.run(token)