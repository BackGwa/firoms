import re
import ext.lumiere as lumiere
import ext.zasok as zasok
import ext.vote as votepy

import secret
import discord

from discord.commands import Option

# [변수] : 기본 변수 설정
bot = discord.Bot()
token = secret.token(True)


# [이벤트] : 봇 온라인
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online)


# [추가 기능] : 투표
@bot.slash_command(
    description='투표를 실시합니다.'
)
async def vote(ctx,
        title: Option(str, '투표의 제목을 입력합니다.'),
        content: Option(str, '투표의 내용을 입력합니다.') = '',
        vote: Option(int, '선택지의 갯수를 입력합니다. 선택지는 2~4개로 제한됩니다.') = 2,
        first: Option(str, '첫 번째 선택지의 이름을 입력합니다.') = '찬성',
        second: Option(str, '두 번째 선택지의 이름을 입력합니다.') = '반대',
        third: Option(str, '세 번째 선택지의 이름을 입력합니다.') = '',
        fourth: Option(str, '네 번째 선택지의 이름을 입력합니다.') = ''
    ):

    result = votepy.v_scan(vote, third, fourth)

    if(result == 'valid'):
        class Button(discord.ui.View):
            @discord.ui.button(label=f'{first}', style=discord.ButtonStyle.primary)
            async def choiceA(self, button: discord.ui.Button, interaction: discord.Interaction):
                await ctx.respond('ButtonEvent FIRST')
                
            @discord.ui.button(label=f'{second}', style=discord.ButtonStyle.primary)
            async def choiceB(self, button: discord.ui.Button, interaction: discord.Interaction):
                await ctx.respond('ButtonEvent SECOND')
            
            if(third != ''):
                @discord.ui.button(label=f'{third}', style=discord.ButtonStyle.primary)
                async def choiceC(self, button: discord.ui.Button, interaction: discord.Interaction):
                    await ctx.respond('ButtonEvent THIRD')
                
                if(fourth != ''):
                    @discord.ui.button(label=f'{fourth}', style=discord.ButtonStyle.primary)
                    async def choiceD(self, button: discord.ui.Button, interaction: discord.Interaction):
                        await ctx.respond('ButtonEvent FOUTRH')
                 
        result = (f'**{title}**\n{content}')
        await ctx.respond(result, view=Button())
        
    else:
        await ctx.respond(result, ephemeral=True)


# [자소크 철학단] : 자소크력 가져오기
@bot.slash_command(
    description='자소크력 가져오기'
)
async def zacalen(ctx,
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
    description='뤼미에르 공화국 숫자 변환기'
)
async def numcvt(ctx, arabic: Option(int, '아라비아 숫자')):
    
    result = lumiere.number(arabic)
    await ctx.respond(f'> **아라비아 숫자** : {arabic}\n> **뤼미에르 숫자** : {result}')


# [호출] : 봇 시작
bot.run(token)