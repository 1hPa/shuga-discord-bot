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

        if message.content==SENSITIVE_WORD:
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(DeleteCog(bot))
