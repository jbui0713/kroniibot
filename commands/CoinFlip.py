import random
from discord.ext import commands
from scipy import rand

class CoinFlip(commands.Cog):

    @commands.command()
    async def flip(self, ctx) -> None:

        result = []
        heads = 0
        tails = 0

        flip = random.randint(0, 1)

        if flip == 0:
            heads += 1
            result.append("heads")
        else:
            tails += 1
            result.append("tails")
        
        await ctx.reply(
            content=f"You got {result[0]}"
        )

