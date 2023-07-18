import discord
from discord.ext import commands
from config import settings


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('MTEyOTc0OTE2NTQzMDI5MjQ5MA.Ghj3Dm.ezKXY4rOyndXlmJHOF3W59CINyRBtlhIOkxs-0')