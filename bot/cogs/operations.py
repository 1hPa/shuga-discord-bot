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
