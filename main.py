import secret
import discord
from discord.commands import Option

bot = discord.Bot()
token = secret.token(True)
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online)
    
@bot.slash_command(guild_ids = secret.server_id(True), description='TestCommand')
async def test(ctx):
    await ctx.respond('TestMessage')

bot.run(token)