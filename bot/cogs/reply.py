import discord
from discord.ext import commands
import random
import asyncio

#Define class
class RepCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Commands creation
    @commands.Cog.listener()
    async def on_message(self, ctx, message):

        await asyncio.sleep(5)

        if message.author.bot:
            return

        if message.content == 'こんにちは':
            await ctx.send('こんにちは')

        if 'w' in message.content:
            await ctx.send(random.choice(('www', '草')))
def setup(bot):
    bot.add_cog(RepCog(bot))
