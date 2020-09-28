import discord
from discord.ext import commands

#Definition class
class RevertCog(commands.Cog):
    #constructor
    def __init__(self, bot):
        self.bot = bot
