from os import getenv
from discord import Activity, ActivityType, Message, opus
from discord.ext import commands
from dotenv import load_dotenv
from speech_recognition import AudioFile, Recognizer, Microphone

from commands.DiceRoll import DiceRoll
from commands.VoiceBot import VoiceBot

import random

load_dotenv()

if (opus_path := getenv("OPUS_PATH")) is not None:
  opus.load_opus(opus_path)

INITIAL_ACTIVITY = Activity(
    name = "What's perfect? Me.",
    type = ActivityType.playing
)

bot = commands.Bot(
  command_prefix = getenv('PREFIX'),
  activity = INITIAL_ACTIVITY
)

PREFIX = getenv('PREFIX')

greets = ['hello kronii', 'hey kronii', 'konnichiwa kronii', 'hi kronii']
replies = ['Kroniichiwa', 'クロニーちは']

@bot.event
async def on_ready():
  print("クロニーは起きます")

@bot.event
async def on_message(message):
  if message.author == bot.user:
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

bot.run(getenv('TOKEN'))