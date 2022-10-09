# [확장] : 투표 및 여론조사


# 투표 유효성 확인
def v_scan(vote, third, fourth):
    if((vote < 2) or (vote > 4)):
        result = ('**선택지의 범위를 초과하였습니다!**\n투표의 선택지는 2~4개로 제한됩니다!') 
        
    elif((vote > 3) and (third == '')) or ((vote > 4) and ((third == '') or (fourth == ''))):
        result = ('**선택지의 이름이 설정되지 않았습니다!**\n투표의 선택지가 2개 이상이라면 선택지의 이름을 입력해야합니다!')
        
        
    elif((vote < 4) and (fourth != '')) or ((vote < 3) and (third != '')):
        result = ('**선택지의 이름이 초과되었거나 잘못된 접근입니다!**\n이러한 명령어는 일부 내용이 손실될 수 있습니다.')
        
    else:
        result = ('valid')
        
    return result