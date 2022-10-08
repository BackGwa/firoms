from http import server
from urllib import request
import ext.lumiere as lumiere
import ext.zasok as zasok

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
    

# [자소크 철학단] : 자소크력 가져오기
@bot.slash_command(
    guild_ids = id,
    description='자소크력 가져오기'
)

async def tozasok(ctx,
        year: Option(int, '계산할 년도를 입력합니다.') = 0,
        monent: Option(int, '계산할 월을 입력합니다.') = 0,
        day: Option(int, '계산할 일을 입력합니다.') = 0,
        hour: Option(int, '계산할 시간을 입력합니다.') = 0,
        minute: Option(int, '계산할 분을 입력합니다.') = 0,
        second: Option(int, '계산할 초를 입력합니다.') = 0
    ):
    
    result = zasok.to_asn(year, monent, day, hour, minute, second)
    await ctx.respond(f'{result}')


# [뤼미에르 공화국] : 숫자 변환기
@bot.slash_command(
    guild_ids = id,
    description='뤼미에르 공화국 숫자 변환기'
)

async def numcvt(ctx, arabic: Option(int, '아라비아 숫자')):
    
    result = lumiere.number(arabic)
    await ctx.respond(f'> **아라비아 숫자** : {arabic}\n> **뤼미에르 숫자** : {result}')


# [호출] : 봇 시작
bot.run(token)