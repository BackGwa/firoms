# [확장] : 피페레제국

ROMAN = 'ABCDEFGHIKLMNOPQRSTVUZaacdefghiklmnopqrstvuz '
ROMAN_LEN = len(ROMAN) - 1
JAELASIA = 'ΑΒΨΔΕΦΓΗΙΚΛΜΝΟΠϘΡΣΤѶΥΖαβψδεφγηικλμνοπϟρστѷυζ '
JAELASIA_LEN = len(ROMAN) - 1


# 피페레 알파벳으로 변환
def rtp(TEXT):
    
    TEXT_LEN = len(TEXT) - 1
    LEN_LOOP = 0
    RMN_LOOP = 0
    CACHE = ''
    RESULT = ''
    OMEGA = True
    
    while(TEXT_LEN >= LEN_LOOP):
        
        CACHE = TEXT[LEN_LOOP]
        OMEGA = True
        
        if(((CACHE == 'O' or CACHE == 'o') and LEN_LOOP != TEXT_LEN) and CACHE == TEXT[LEN_LOOP + 1]):
            if(CACHE == 'O'):
                RESULT += 'Ω'
                LEN_LOOP += 1
            else:
                RESULT += 'ω'
                LEN_LOOP += 1
                
            OMEGA = False
        
        while((ROMAN_LEN >= RMN_LOOP) and OMEGA):
            
            if(ROMAN[RMN_LOOP] == CACHE):
                RESULT += JAELASIA[RMN_LOOP]
                RMN_LOOP = 0
                break
            else:
                RMN_LOOP += 1
            
        LEN_LOOP += 1
    
    return RESULT


# 로마자로 변환
def ptr(TEXT):
    
    TEXT_LEN = len(TEXT) - 1
    LEN_LOOP = 0
    RMN_LOOP = 0
    CACHE = ''
    RESULT = ''
    
    while(TEXT_LEN >= LEN_LOOP):
        
        CACHE = TEXT[LEN_LOOP]
        
        while(JAELASIA_LEN >= PPR_LOOP):
            
            if(JAELASIA[PPR_LOOP] == CACHE):
                RESULT += ROMAN[PPR_LOOP]
                PPR_LOOP = 0
                break
            
            elif(CACHE == 'Ω'):
                RESULT += 'OO'
                PPR_LOOP = 0
                break
            
            elif(CACHE == 'ω'):
                RESULT += 'oo'
                PPR_LOOP = 0
                break
            
            else:
                PPR_LOOP += 1
            
        LEN_LOOP += 1
    
    return RESULT