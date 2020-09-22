from discord.ext import commands
import discord
'''
GRASS = [
    '草',
    'くさ',
    'grass'
]
'''

class RxnCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if '草' in message.content:
            await message.channel.send(file=discord.File('../../img/grass.png'))

def setup(bot):
    bot.add_cog(RxnCog(bot))
