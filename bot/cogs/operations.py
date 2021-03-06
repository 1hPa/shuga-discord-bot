import discord
from discord.ext import commands
import random

#Definition class
class OpCog(commands.Cog):
    #Constructor
    def __init__(self, bot):
        self.bot = bot

    #Make command
    @commands.command()
    async def op(self, ctx):
        while True:
            left = random.randrange(1000)
            right = random.randrange(1000)
        '''
        2 digits or more
        '''
            if len(str(left)) and len(str(right)) >= 2:
                break

    #Answer
    ans = left+right

    #Output message
    await ctx.send('Add the following numbers')
    await ctx.send(str(left)+'+'+str(right))

    @commands.comand()
    async def opans(self, ctx, ansin):
        #Compare with answer
        if ansin == ans:
            await ctx.send('Correct!!')
        else:
            await ctx.send('Wrong answer...\nans = '+str(ans))

def setup(bot):
    bot.add_cog(OpCog(bot))
