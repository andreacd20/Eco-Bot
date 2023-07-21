import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def info(ctx):
    await ctx.send(f'Hi! Im Happy Hazel, your friendly eco bot! Im here to teach you ways to live a more eco-friendly lifestyle! Try typing !lifestyle for a start! Remember the Earth is our only home. Lets take care of it properly!')
    img_name = random.choice(os.listdir('5. earthmeme'))
    with open(f'5. earthmeme/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def lifestyle(ctx):
    await ctx.send(f'Here are a few things you can implement in your lifestyle to help the enviroment!')
    await ctx.send(f'1. Bring your very own water bottle!')
    await ctx.send(f'2. Carry a shopping bag around, just in case!')
    await ctx.send(f'3. Think twice before you buy something!')
    await ctx.send(f'4. Ditch one time use items from now on!')
    await ctx.send(f'5. Eat local and organic food!')
    await ctx.send(f'6. Eat your foooood! Reduce food waste.')
    await ctx.send(f'7. Ride a bike or go on a walk if its close by! This is also healthier for you :)')
    await ctx.send(f'8. Type !recycle to see some fun ideas you can transform your waste products into!')

@bot.command()
async def recycle(ctx):
    img_name2 = random.choice(os.listdir('5. recyclingideas'))
    with open(f'5. recyclingideas/{img_name2}', 'rb') as f:
        picture2 = discord.File(f)
    await ctx.send(file=picture2)

bot.run("TOKEN")
