# [확장] : 투표 및 여론조사
import discord

# 에러 메세지
def errmsg(index):
    
    if(index == 0):
        result = discord.Embed(title='**투표가 완료되었습니다!**', description='소중한 의견을 주셔서 감사드립니다!', color=discord.Color.green())
    elif(index == 1):
        result = discord.Embed(title='**투표가 반영되지 않았습니다!**', description='중복투표를 하거나 여러 번 투표하실 수 없습니다!', color=discord.Color.red())
    elif(index == 2):
        result = discord.Embed(title='**선택지의 범위를 초과하였습니다!**', description='투표의 선택지는 2~4개로 제한됩니다!', color=discord.Color.red())
    elif(index == 3):
        result = discord.Embed(title='**선택지의 이름이 설정되지 않았습니다!**', description='투표의 선택지가 2개 이상이라면 선택지의 이름을 입력해야합니다!', color=discord.Color.red())
    elif(index == 4):
        result = discord.Embed(title='**선택지의 이름이 초과되었거나 잘못된 접근입니다!**', description='이러한 명령어는 일부 내용이 손실될 수 있습니다.', color=discord.Color.red())

    return result

# 투표 프로그래스바
def value(count):
    
    result = ''
    loop = 0
    
    while(count > loop):
        result += '■'
        loop += 1
    
    return result

# 투표 새로고침
def msg_refrash(title, content, vote, count, a, b, c, d):
    
    valueA = value(count[0])
    valueB = value(count[1])
    valueC = value(count[2])
    valueD = value(count[3])

    if(vote == 2):                   
        result = (f'**{title}**\n{content}\n' 
                  f'> {a} ( {count[0]}표 ) : {valueA}\n'
                  f'> {b} ( {count[1]}표 ) : {valueB}')
        
    elif(vote == 3):
        result = (f'**{title}**\n{content}\n' 
            f'> {a} ( {count[0]}표 ) : {valueA}\n'
            f'> {b} ( {count[1]}표 ) : {valueB}\n'
            f'> {c} ( {count[2]}표 ) : {valueC}\n'          
            )
        
    elif(vote == 4):
        result = (f'**{title}**\n{content}\n' 
            f'> {a} ( {count[0]}표 ) : {valueA}\n'
            f'> {b} ( {count[1]}표 ) : {valueB}\n'
            f'> {c} ( {count[2]}표 ) : {valueC}\n'
            f'> {d} ( {count[3]}표 ) : {valueD}\n'          
            )
        
    return result