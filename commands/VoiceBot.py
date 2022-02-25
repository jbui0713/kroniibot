from os import getenv
from threading import Thread
from discord import FFmpegPCMAudio, VoiceClient
from discord.ext import commands
from speech_recognition import Microphone, Recognizer
import asyncio

class VoiceBot(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.voice_client: VoiceClient | None = None

        if (str_id := getenv("DISCORD_ID")) is not None:
            self.DISCORD_ID = int(str_id)

        thread = Thread(target = self.listener)
        thread.daemon = True
        thread.start()

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after) -> None:

        member_id: int = member.id

        if member_id != self.DISCORD_ID:
            return

        if after.channel is not None:
            if self.voice_client is not None:
                await self.voice_client.disconnect()
                
            self.voice_client = await after.channel.connect()

        elif self.voice_client is not None:
            await self.voice_client.disconnect()
            self.voice_client = None
