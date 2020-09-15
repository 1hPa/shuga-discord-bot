from discord.ext import tasks, commands

CHANNEL_ID = 728821929103851521

#Definition class
class GreetingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @tasks.loop(seconds=60)
    async def loop():
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('おはよう')
#Loop processing
loop.start()

def setup(bot):
    bot.add_cog(GreetingCog(bot))
