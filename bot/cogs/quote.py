import discord
from discord.ext import commands
from datetime import datetime 

class QuoteCog(commands.Cog):
    #constructor
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def quote(self, ctx):
        await ctx.send(random.choice(KOSEN_QUOTE))
