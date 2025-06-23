import os
import dotenv
import discord
from discord.ext import commands, tasks
import logging

dotenv.load_dotenv()
bot_token = os.getenv("BOT_TOKEN")

handler = logging.FileHandler(filename="log.log", mode="w")

intents = discord.Intents.all()


bot = commands.Bot(command_prefix="*", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    await message.channel.send(f"{message.author} a dit {message.content}")
    

bot.run(bot_token, log_handler=handler)