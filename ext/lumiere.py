# [확장] : 뤼미에르 공화국


# [명령어] : 숫자 변환기
def number(arabic):
    
    number_define = ['za', 'ho', 'san', 'ni', 'chi', 'la', 'pi', 'kan', 'kain', 'laio']
    result = ''
        
    for number in str(arabic):
        result += number_define[int(number)]
    
    return result