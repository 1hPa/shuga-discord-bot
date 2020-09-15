import discord
from discord.ext import commands
from datetime import datetime 
import random

KOSEN_QUOTE = [
    '微積は高専生の九九だからねー',
    'ちーがーうーよー'
]

class QuoteCog(commands.Cog):
    #constructor
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def quote(self, ctx):
        await ctx.send(random.choice(KOSEN_QUOTE))

def setup(bot):
    bot.add_cog(QuoteCog(bot))
