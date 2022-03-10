from ast import alias
from discord.ext import commands
from discord import File
import random
import os

lines = ["oke", "we star lab", "we start lab"]

class YaoWang(commands.Cog):

    @commands.command(aliases=['Yw', 'YW', 'yW'])
    async def yw(self, ctx) -> None:
        
        random_reply = random.choice(lines)
        filepath = 'assets/'
        img = os.listdir(filepath)
        random_yao = random.choice(img)

        await ctx.send(
            content=f"<@!173271142897811456> {random_reply}",
            file=File(filepath+random_yao),
            delete_after=120
        )
    
    @commands.command(alias=['evil yao wang'])
    async def evil(self, ctx) -> None:
        
        img = 'assets/evilyaowang.jpg'

        await ctx.send(
            content=f"Did I hear evil?",
            file=File(img),
            delete_after=120
        )        
