import discord
from discord.ext import commands
from bot_logic import gen_pass
from bot_logic import carta_forbice_sasso

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {bot.user}')

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
        await ctx.send()
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
  
bot.run("token")