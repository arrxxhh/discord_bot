import discord
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$hello'):
    await message.channel.send('hello!')
  if message.content.startswith('$how are you'):
    await message.channel.send('I am fine.')


client.run(os.getenv('TOKEN'))
