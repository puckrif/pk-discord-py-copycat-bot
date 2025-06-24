import os
import dotenv
import discord
from discord.ext import commands, tasks
import json
import logging

dotenv.load_dotenv()
bot_token = os.getenv("BOT_TOKEN")

handler = logging.FileHandler(filename="log.log", mode="w")

intents = discord.Intents.all()


bot = commands.Bot(command_prefix="*", intents=intents)


AUTHORIZED_FILE = "authorized_channels.json"

def load_authorized_channels():
    if os.path.exists(AUTHORIZED_FILE):
        with open(AUTHORIZED_FILE, "r") as file:
            try:
                ids = json.load(file)
                return ids
            except:
                return []
    return []

def save_authorized_channels():
    with open(AUTHORIZED_FILE, "w") as file:
        json.dump(authorized_channels, file)

authorized_channels = load_authorized_channels()



@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.channel.id in authorized_channels :
        await message.channel.send(f"{message.author} a dit {message.content}")
    await bot.process_commands(message)


@bot.command()
async def authorize(ctx):
    if ctx.channel.id not in authorized_channels:
        authorized_channels.append(ctx.channel.id)
        save_authorized_channels()
        await ctx.send("Ce salon est maintenant autorisé !")
    else:
        await ctx.send("Ce salon est déjà autorisé.")

@bot.command()
async def unauthorize(ctx):
    if ctx.channel.id in authorized_channels:
        authorized_channels.remove(ctx.channel.id)
        save_authorized_channels()
        await ctx.send("Ce salon n'est plus autorisé !")
    else:
        await ctx.send("Ce salon n'est déjà pas autorisé.")

@bot.command()
async def isauthorized(ctx):
    if ctx.channel.id in authorized_channels :
        await ctx.send("Oui, ce salon est autorisé.")
    else :
        await ctx.send("Non, ce salon n'est pas autorisé.")

@bot.command()
async def unauthorize_all(ctx):
    authorized_channels.clear()
    save_authorized_channels()
    await ctx.send("Plus aucun channel n'est authorisé !")

@bot.command()
async def puck(ctx):
    embed = discord.Embed(
        title="Puck le GOAT",
        color=discord.Color.blue()
    )
    embed.set_image(url="https://static.wikia.nocookie.net/vsbattles/images/8/8d/Chestnut_Puck.webp/revision/latest/scale-to-width-down/400?cb=20240428105641")
    await ctx.send(embed=embed)



bot.run(bot_token, log_handler=handler)