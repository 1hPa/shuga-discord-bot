import discord
from discord.ext import commands

#Definition class
class DakutenCog(commands.Cog):
    #constructor
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dakuten(self, ctx, msg):
        strlist = msg
        await ctx.send('゛'.join(list(strlist))+'゛')
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(DakutenCog(bot))
