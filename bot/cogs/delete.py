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
    async def on_message(self, ctx, message):
        for improper in SENSITIVE_WORD:
            if message==improper:
                await ctx.message.delete()
