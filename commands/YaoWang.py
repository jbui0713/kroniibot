from discord.ext import commands
from discord import File
import random

lines = ["oke", "we star lab", "we start lab"]

class YaoWang(commands.Cog):

    @commands.command(aliases=['Yw', 'YW', 'yW'])
    async def yw(self, ctx) -> None:
        
        random_reply = random.choice(lines)

        await ctx.send(
            content=f"<@!173271142897811456> {random_reply}",
            file=File("assets/yaowang.jpg"),
            delete_after=120
        )
