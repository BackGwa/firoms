import ext.lumiere as lumiere
import ext.zasok as zasok
import ext.vote as votepy

import secret
import discord
import time

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
    description='투표를 실시합니다'
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

    count = [0, 0, 0, 0]

    if((vote < 2) or (vote > 4)):
        await ctx.respond('**선택지의 범위를 초과하였습니다!**\n투표의 선택지는 2~4개로 제한됩니다!', ephemeral=True)
        
    elif((vote > 3) and (third == '')) or ((vote > 4) and ((third == '') or (fourth == ''))):
        await ctx.respond('**선택지의 이름이 설정되지 않았습니다!**\n투표의 선택지가 2개 이상이라면 선택지의 이름을 입력해야합니다!', ephemeral=True)
        
    elif((vote < 4) and (fourth != '')) or ((vote < 3) and (third != '')):
        await ctx.respond('**선택지의 이름이 초과되었거나 잘못된 접근입니다!**\n이러한 명령어는 일부 내용이 손실될 수 있습니다.', ephemeral=True)
            
    else:
        class Button(discord.ui.View):
            
            global dataid
            dataid = []
            
            @discord.ui.button(label=f'{first}', style=discord.ButtonStyle.primary)
            async def choiceA(self, button: discord.ui.Button, interaction: discord.Interaction):
                
                global dataid
                global sendmsg
                
                if(interaction.user.id in dataid):
                    vote_result = votepy.errmsg(1)
                else:
                    vote_result = votepy.errmsg(0)
                    dataid += [interaction.user.id]
                    count[0] += 1
                    
                    editmsg = votepy.msg_refrash(title, content, vote, count, first, second, third, fourth)
                    await interaction.message.edit(content=f'{editmsg}')

                await ctx.respond(vote_result, ephemeral=True)
                
            @discord.ui.button(label=f'{second}', style=discord.ButtonStyle.primary)
            async def choiceB(self, button: discord.ui.Button, interaction: discord.Interaction):
                
                global dataid
                global sendmsg
                
                if(interaction.user.id in dataid):
                    vote_result = votepy.errmsg(1)
                else:
                    vote_result = votepy.errmsg(0)
                    dataid += [interaction.user.id]
                    count[1] += 1
                    
                    editmsg = votepy.msg_refrash(title, content, vote, count, first, second, third, fourth)
                    await interaction.message.edit(content=f'{editmsg}')
                
                await ctx.respond(vote_result, ephemeral=True)

            if(third != ''):
                @discord.ui.button(label=f'{third}', style=discord.ButtonStyle.primary)
                async def choiceC(self, button: discord.ui.Button, interaction: discord.Interaction):
                    
                    global dataid
                    global sendmsg
                    
                    if(interaction.user.id in dataid):
                        vote_result = votepy.errmsg(1)
                    else:
                        vote_result = votepy.errmsg(0)
                        dataid += [interaction.user.id]
                        count[2] += 1
                        
                        editmsg = votepy.msg_refrash(title, content, vote, count, first, second, third, fourth)
                        await interaction.message.edit(content=f'{editmsg}')
                    
                    await ctx.respond(vote_result, ephemeral=True)
                
                if(fourth != ''):
                    @discord.ui.button(label=f'{fourth}', style=discord.ButtonStyle.primary)
                    async def choiceD(self, button: discord.ui.Button, interaction: discord.Interaction):
                        
                        global dataid
                        global sendmsg
                        
                        if(interaction.user.id in dataid):
                            vote_result = votepy.errmsg(1)
                        else:
                            vote_result = votepy.errmsg(0)
                            dataid += [interaction.user.id]
                            count[3] += 1
                            
                            editmsg = votepy.msg_refrash(title, content, vote, count, first, second, third, fourth)
                            await interaction.message.edit(content=f'{editmsg}')
                        
                        await ctx.respond(vote_result, ephemeral=True)
        
        if(vote == 2):              
            result = (f'**{title}**\n{content}\n> {first} : \n> {second} : ')
        elif(vote == 3):
            result = (f'**{title}**\n{content}\n> {first} : \n> {second} : \n> {third} : ')
        elif(vote == 4):
            result = (f'**{title}**\n{content}\n> {first} : \n> {second} : \n> {third} : \n> {fourth} : ')
        
        global sendmsg
        sendmsg = await ctx.respond(result, view=Button())
        

# [자소크 철학단] : 자소크력 가져오기
@bot.slash_command(
    description='서력 날짜를 자소크력으로 변환합니다.'
)
async def zacalen(ctx,
        year: Option(int, '계산할 년도를 입력합니다.') = 0,
        monent: Option(int, '계산할 월을 입력합니다.') = 0,
        day: Option(int, '계산할 일을 입력합니다.') = 0,
        hour: Option(int, '계산할 시간을 입력합니다.') = 0,
        minute: Option(int, '계산할 분을 입력합니다.') = 0,
        second: Option(int, '계산할 초를 입력합니다.') = 0
    ):
    
    result = zasok.zacalen(year, monent, day, hour, minute, second)
    await ctx.respond(f'{result}')


# [자소크 철학단] : 자소크력으로 서력 가져오기
@bot.slash_command(
    description='자소크력으로 서력 날짜를 가져옵니다.'
)
async def inzacalen(ctx,
        year: Option(int, '계산할 년도를 입력합니다.'),
        monent: Option(int, '계산할 월을 입력합니다.') = 1,
        day: Option(int, '계산할 일을 입력합니다.') = 1
    ):
    
    result = zasok.inzacalen(year, monent, day)
    await ctx.respond(f'{result}')


# [뤼미에르 공화국] : 숫자 변환기
@bot.slash_command(
    description='뤼미에르 공화국의 숫자로 변환합니다.'
)
async def numcvt(ctx, arabic: Option(int, '아라비아 숫자')):
    
    result = lumiere.number(arabic)
    await ctx.respond(f'> **아라비아 숫자** : {arabic}\n> **뤼미에르 숫자** : {result}')


# [호출] : 봇 시작
bot.run(token)