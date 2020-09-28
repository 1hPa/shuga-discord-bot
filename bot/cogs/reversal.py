import discord
from discord.ext import commands

#Definition class
class ReversalCog(commands.Cog):
    #constructor
    def __init__(self, bot):
        self.bot = bot

    @commands.command(alias=['rev'])
    async def reversal(self, ctx, msg):
        strlist = msg
        await ctx.send(''.join(list(reversed(strlist)))+'\nBy'+ctx.author.mention)
        await ctx.message.delete()
        await ctx.send('reverseコマンドを使用しました。')
def setup(bot):
    bot.add_cog(ReversalCog(bot))
