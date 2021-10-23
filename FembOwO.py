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
#prefix and command.bot=bot
bot = commands.Bot(command_prefix=config.get("prefix"))

#file logging   CRITICAL, ERROR, WARNING, INFO and DEBUG
logging.basicConfig(level=logging.INFO)
"""
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
"""
@bot.command()
async def ping(ctx):
    await ctx.send(f'Ping: {round(bot.latency * 1000)}ms')
@bot.command()
async def helping(ctx):
    embed = discord.Embed(
        title = 'Help page',
        description = 'This is the help page (WIP)'
    )
    embed.set_image(url='https://discordemoji.com/assets/emoji/2788_stupid.png')
    embed.set_footer(text='Wut')
    await ctx.send(embed = embed)
#not working
@bot.command()
async def time(ctx):
    date = datetime.datetime.now()
    to_send = 'The time is:'
    await ctx.send(to_send)
    print('timetelling test success!')
#not working
"""
@bot.event
async def on_member_join(member):
    print('welcome member #0 test success!')
    guild = member.guild
    print('welcome member #1 test success!')
    if guild.system_channel is not None:
        to_send = 'Welcome {member.mention} to {guild.name}!'
        await guild.system_channel.send(to_send)
        print('welcome member #2 test success!')
"""
#activated when bot ready
@bot.event
async def on_ready():
    start_time = datetime.datetime.now()
    print('We have logged in as {0.user} (ID: {0.user.id}) \nTime:'.format(bot), start_time, '\nPrefix:', config.get("prefix"))
    print('----------------------------------------------------------------------')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="ur mum"))

#how the fuck is this working?
class MyClient(discord.Client):
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)
intents = discord.Intents.default()
intents.members = True
client = MyClient(intents=intents)

#token
token = config.get("token")
bot.run(token)