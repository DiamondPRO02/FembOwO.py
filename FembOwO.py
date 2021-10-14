import discord
import logging

client = discord.Client()

#logging.basicConfig(level=logging.INFO)
#file logging
logger = logging.getLogger('discord')
#CRITICAL, ERROR, WARNING, INFO and DEBUG
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!', mention_author=True)
        
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#token
client.run('token')