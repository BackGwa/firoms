# [확장] : 투표 및 여론조사


# 에러 메세지
def errmsg(index):
    
    if(index == 1):
        result = ('**투표가 반영되지 않았습니다!**\n중복투표를 하거나 여러 번 투표하실 수 없습니다!')
    else:
        result = ('**투표가 완료되었습니다!**')
    
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
                  f'{a} ( {count[0]}표 ) : {valueA}\n'
                  f'{b} ( {count[1]}표 ) : {valueB}')
        
    elif(vote == 3):
        result = (f'**{title}**\n{content}\n' 
            f'{a} ( {count[0]}표 ) : {valueA}\n'
            f'{b} ( {count[1]}표 ) : {valueB}\n'
            f'{c} ( {count[2]}표 ) : {valueC}\n'          
            )
        
    elif(vote == 4):
        result = (f'**{title}**\n{content}\n' 
            f'{a} ( {count[0]}표 ) : {valueA}\n'
            f'{b} ( {count[1]}표 ) : {valueB}\n'
            f'{c} ( {count[2]}표 ) : {valueC}\n'
            f'{d} ( {count[3]}표 ) : {valueD}\n'          
            )
        
    return result