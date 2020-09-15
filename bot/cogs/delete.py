from discord.ext import commands
import discord

SENSITIVE_WORD = [
    'ちんちん'
]

#Definition class
class DeleteCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content in SENSITIVE_WORD:
            await message.delete()
            await message.channel.send(message.author.name+'の不適切なメッセージを削除しました。')

def setup(bot):
    bot.add_cog(DeleteCog(bot))
