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
    async def on_message(self, message):

        if message.author.bot:
            return

        if 'しゅが' in message.content:
            await asyncio.sleep(1)
            await message.channel.send('なぁ〜に？')

        if 'おやすみ' in message.content:
            await asyncio.sleep(3)
            await message.channel.send('(๑´•ω•)੭ ੈおやすみなさい')

        if message.content.endwith('w'):
            await asyncio.sleep(3)
            await message.channel.send(random.choice(('www', '草')))

        if '煽り' in message.content:
            await asyncio.sleep(1)
            await message.channel.send('煽るな')
def setup(bot):
    bot.add_cog(RepCog(bot))
