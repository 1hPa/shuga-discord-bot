import discord
from discord.ext import commands

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
        if len(str(left)) >= 2 and len(str(right)) >= 2:
            break

    #Answer
    ans = left+right

    #Output message
    print('Add the following numbers')
    print(str(left)+'+'+str(right))
