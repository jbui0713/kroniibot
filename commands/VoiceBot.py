from os import getenv
from threading import Thread
from discord import AudioSource, FFmpegPCMAudio, VoiceClient
from discord.ext import commands
from speech_recognition import Microphone, Recognizer
import asyncio

ffmpeg_path = "ffmpeg.exe"

class VoiceBot(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.voice_client: VoiceClient | None = None

        self.mic = Microphone()
        self.recognizer = Recognizer()

        self.recognizer.energy_threshold = 1500

        if (str_id := getenv("DISCORD_ID")) is not None:
            self.DISCORD_ID = int(str_id)

        thread = Thread(target = self.listen_event)
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
    
    def listen_event(self):
        with self.mic as mic:
            while True:
                self.recognizer.adjust_for_ambient_noise(
                    self.mic, duration=0.5
                )
                audio = self.recognizer.listen(mic)
                try:
                    print("Trying")
                    text = self.recognizer.recognize_google(
                        audio
                    )
                    print ('Your input:',text)
                    if "hello" in text or "hi" in text:
                        audio_source = FFmpegPCMAudio(
                            source="voice/hello-kroniichiwa.mp3", executable=ffmpeg_path)
                        self.play_audio(audio_source)
                    elif "baca" in text.lower():
                        audio_source = FFmpegPCMAudio(
                            source="voice/baka.mp3")
                        self.play_audio(audio_source)
                except:
                    print ("Come again?")
                finally:
                    text = ""
 
    def play_audio(self, audio_source: AudioSource):
        if self.voice_client is not None:
            self.voice_client.play(audio_source)

    @commands.command(name="play")
    async def play_command(self, ctx) -> None:
        audio_source = FFmpegPCMAudio(
            source="voice/ribbon.mp3", executable=ffmpeg_path
        )
        if self.voice_client is not None:
            self.voice_client.play(audio_source)