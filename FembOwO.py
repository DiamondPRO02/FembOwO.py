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

logging.basicConfig(level=logging.INFO)
#file logging
"""
logger = logging.getLogger('discord')
#CRITICAL, ERROR, WARNING, INFO and DEBUG
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
"""

@client.event
async def on_message(message):
    prefix = config.get("prefix")
    if message.author.id == client.user.id:
        return
#write if prefix !== message content startwith => return
    if message.content.startswith(prefix + 'hello'):
        await message.channel.send('Hello!', mention_author=True)
        print('hello test success!')

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
    print('We have logged in as {0.user} (ID: {0.user.id}) \nTime:'.format(client), start_time)
    print('----------------------------------------------------------------------')

#token
token = config.get("token")
client.run(token)