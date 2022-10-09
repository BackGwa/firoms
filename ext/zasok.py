# [확장] : 자소크 철학단

from sat_datetime import SatDatetime
from datetime import datetime


# [명령어] : 서력으로 자소크력 가져오기
def zacalen(year, month, day, hour, minute, second):
    
    now = datetime.now()
    now = datetime(
            year if year else now.year,
            month if month else now.month,
            day if day else now.day,
            hour if hour else now.hour,
            minute if minute else now.minute,
            second if second else now.second
        )
    ZasokNow = SatDatetime.get_from_datetime(now)
    
    result = (f'>   **[UTC]**   __{now.year}년 {now.month:02d}월 {now.day:02d}일 {now.hour:02d}시 {now.minute:02d}분 {now.minute:02d}초__\n'
              f'>   **[ASN]**   __{ZasokNow.year}년 {ZasokNow.month:02d}월 {ZasokNow.day:02d}일 {ZasokNow.hour:02d}시 {ZasokNow.minute:02d}분 {int(ZasokNow.second):02d}초__')
    
    return result


# [명령어] : 자소크력으로 서력 가져오기
def inzacalen(year, month, day):
    
    ZasokNow = SatDatetime(year, month, day)
    utc = ZasokNow.to_datetime()
    
    result = (f'>   **[ASN]**   __{year}년 {month:02d}월 {day:02d}일__\n'
              f'>   **[UTC]**   __{utc.year}년 {utc.month:02d}월 {utc.day:02d}일__')
    
    return result