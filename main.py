import ext.lumiere as lumiere

import secret
import discord

from discord.commands import Option

# [변수] : 기본 변수 설정
bot = discord.Bot()
token = secret.token(True)
id = secret.server_id(True)


# [이벤트] : 봇 온라인
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online)
    

# [뤼미에르 공화국] : 숫자 변환기
@bot.slash_command(
    guild_ids = id,
    description='뤼미에르 공화국 숫자 변환기'
)

async def numcvt(ctx, arabic: Option(int, '아라비아 숫자')):
    
    result = lumiere.number(arabic)
    await ctx.send(f'> **아라비아 숫자** : {arabic}\n> **뤼미에르 숫자** : {result}')


# [호출] : 봇 시작
bot.run(token)