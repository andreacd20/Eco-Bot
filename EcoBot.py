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
async def bye(ctx):
    await ctx.send(f'\U0001f44b')
    
@bot.command()
async def info(ctx):
    await ctx.send(f'Hi! Im Happy Hazel, your friendly eco bot :)\n \n Im here to teach you ways to live a more eco-friendly lifestyle!\n Remember! Earth is our only home. Lets take care of it properly!\n \n Try typing !lifestyle for a start!')
    img_name = random.choice(os.listdir('5. earthmeme'))
    with open(f'5. earthmeme/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def lifestyle(ctx):
    await ctx.send(f'Here are a few actions you can implement in your daily life to help the enviroment!\n 1. Bring your very own water bottle!\n 2. Carry a shopping bag around, just in case!\n 3. Think twice before you buy something!\n 4. Ditch one time use items from now on!\n 5. Eat local and organic food!\n 6. Eat your foooood! Reduce food waste.\n 7. Ride a bike or go on a walk if its close by! Its also healthier for you :)\n 8. Type !recycle to see some fun ideas you can transform your waste products into!\n \n \U0001f642 \U0001f642')

@bot.command()
async def recycle(ctx):
    img_name2 = random.choice(os.listdir('5. recyclingideas'))
    with open(f'5. recyclingideas/{img_name2}', 'rb') as f:
        picture2 = discord.File(f)
    await ctx.send(file=picture2)

bot.run("TOKEN")
