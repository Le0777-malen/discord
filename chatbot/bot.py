import discord
import random
import os

from discord.ext import commands
from bot_logic import gen_pass
from bot_logic import carta_forbice_sasso
from bot_logic import get_dog_image_url
from bot_logic import mt\


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {bot.user}')

print(os.listdir('images'))

@bot.command()
async def on_message(message):
    if message.author == bot.user:
        return


@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def arrivederci(ctx):
    await ctx.send(f"\U0001f642{bot.user}!") 
  
@bot.command()
async def giochiamo(ctx):
    await ctx.send(f"la mia mossa è " + carta_forbice_sasso())
    
@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)
@bot.command()
async def meteo(ctx):
    await ctx.send(mt())

@bot.command()
async def mem(ctx):
    choice = random.choice(os.listdir('images'))

    with open(f'images/{choice}', 'rb') as f:
    # Memorizziamo il file della libreria di Discord convertito in questa variabile!
        picture = discord.File(f)
    # Possiamo quindi inviare questo file come parametro!
    await ctx.send(file=picture)




@bot.command('dog')
async def dog(ctx):
    '''Una volta chiamato il comando dog, il programma richiama la funzione get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)
       
  
bot.run("token")
