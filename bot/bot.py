from discord.ext import commands
import os

token = os.environ['DISCORD_BOT_TOKEN']

#class definition
class Bot(commands.Bot):
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
