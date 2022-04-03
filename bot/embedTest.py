import disnake, random
from disnake.ext import commands, tasks
from disnake import Intents, Embed
from disnake.ext.commands.core import has_permissions
from os import environ
from config import TOKEN
import pygsheets

class shiinaBot:
    def __init__(self):
        self.token = TOKEN

    def main(self):
        intents = Intents.all()
        bot = commands.Bot(command_prefix="s!", intents=intents)
        
        @bot.event
        async def on_ready():
            print(f">> {bot.user.name} is ready")

        @bot.command(name="e")
        async def embedTest(ctx):
            embed = Embed(title = "TEST", description="測試")
            embed.set_image(url="http://pbs.twimg.com/media/FOduA6fWQA8NX30.jpg")
            embed.set_image(url="http://pbs.twimg.com/media/FOduBODXoBAcMFD.jpg")
            await ctx.channel.send(embed=embed)

        bot.run(self.token)

if __name__ == "__main__":
    # print("Hello World!")
    bot = shiinaBot()
    bot.main()