from discord.ext import commands
import discord

#Definition class
class DeleteCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
