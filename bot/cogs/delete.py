from discord.ext import commands
import discord

SENSITIVE_WORD = [
    'ちんちん'
]

#Definition class
class DeleteCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content in SENSITIVE_WORD:
            await message.channel.delete()

def setup(bot):
    bot.add_cog(DeleteCog(bot))
