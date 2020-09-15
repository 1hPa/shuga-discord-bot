from discord.ext import commands
import traceback
import os

token = os.environ['DISCORD_BOT_TOKEN']

#Store cogs
INITIAL_EXTENSIONS = [
    'cogs.reply',
    'cogs.delete',
    'cogs.quote'
]

#class definition
class Bot(commands.Bot):

    #Bot Constructor
    def __init__(self, command_prefix):

        #Pass to the superclass and run
        super().__init__(command_prefix)

        #Loading cog
        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()

    #call when ready
    async def on_ready(self):
        print('-----')
        print(self.user.name)
        print(self.user.id)
        print('-----')

#Bot instantiation and launch process
if __name__ == '__main__':
    bot = Bot(command_prefix='!')
    bot.run(token)
