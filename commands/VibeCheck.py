from discord.ext import commands
import discord
import random


class VibeCheck(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def vibecheck(self, ctx, member: discord.Member) -> None:

        voice_channel = await retrieve_acitive_voice
        voice_client = discord.VoiceClient = await voice

        disconnect_chance = 0.5
        kick_chance = 0.3


        #member=157981780534755328


        if random.random() < disconnect_chance:
            print ("disconnected")
            await member.move_to(None)

        elif random.random() < kick_chance:
            print ("kicked")
