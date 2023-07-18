import discord
from discord.ext import commands
from config import settings


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


#@bot.command()
#async def ping(ctx):
#   await ctx.send('pong')

class MyView(discord.ui.View):                                                                                   # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.primary, emoji="😎")                        # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("You clicked the button!")                                       # Send a message when the button is clicked 

@bot.command()
async def helps(ctx, arg=None):
    author = ctx.message.author
    if arg == None:
        await ctx.send (f' {author} Введите: \n !helps main\n !helps PB')
    elif arg == 'main' :
        await ctx.send(f' {author} Здесь вы можете увидеть весь список доступных функций бота на данном этапе')
    elif arg == 'PB' :
        await ctx.send(f' {author} Для того, чтобы увидеть дату проведения ближайших полковых боев - напишите АААА')
    else :
        await ctx.send(f' {author} такой команды нет') 
bot.run('MTEzMDg3MzA4NDY2NTEzNTEzNQ.GqHQHT.pTWaaRVNcVi0xUsi_aVhNyWzwBEwiXyVAbyIrg')