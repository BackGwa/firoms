# [확장] : 자소크 철학단

import sat_datetime as SatTime
import datetime


# [명령어] : 자소크력 가져오기
def to_asn(year, month, day, hour, minute):
    
    EarthNow = datetime.now()
    ZasokNow = datetime(
            year if year else ZasokNow.year,
            month if month else ZasokNow.month,
            day if day else ZasokNow.day,
            hour if hour else ZasokNow.hour,
            minute if minute else ZasokNow.minute
        )
    ZasokNow = SatTime.get_from_datetime(ZasokNow)
    
    result = (f'> {EarthNow.year}년 {EarthNow.month}월 {EarthNow.day}일 {EarthNow.hour}시 {EarthNow.minute}분\n'
              f'> {ZasokNow.year}년 {ZasokNow.month}월 {ZasokNow.day}일 {ZasokNow.hour}시 {ZasokNow.minute}분')
    
    return result