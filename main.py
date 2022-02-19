import os
import discord
import random
from dotenv import load_dotenv
from commands.DiceRoll import DiceRoll
from commands.VoiceBot import VoiceBot
load_dotenv()

TOKEN = os.environ['TOKEN']
PREFIX = os.environ['PREFIX']
client = discord.Client()

greets = ['hello kronii', 'hey kronii', 'konnichiwa kronii', 'hi kronii']
replies = ['Kroniichiwa', 'クロニーちは']

@client.event
async def on_ready():
  print("クロニーは起きます")

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if any(word in msg.lower() for word in greets):
    random_reply = random.choice(replies)
    author_id = message.author.id
    await message.channel.send('{0} <@!{1}>'.format(random_reply, author_id))
  
  if msg.startswith(PREFIX+'roll'): #?roll 1d20
    dice_input = msg.split(PREFIX+'roll ', 1)[1]
    await message.reply(DiceRoll(dice_input).message)
      
  if msg.startswith(PREFIX+'hello' or PREFIX+'hi' or PREFIX+'konnichiwa'):
    return

client.run(TOKEN)