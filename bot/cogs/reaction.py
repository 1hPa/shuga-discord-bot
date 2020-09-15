from discord.ext import commands
import discord

class RxnCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if GRASS in message.content:
            await message.channel.send(../../img/grass.png)
