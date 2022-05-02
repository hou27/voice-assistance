import datetime
from stt_tts import tts

def get_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    tts(f"현재 시각은 {time}입니다.")
    return time

def get_day():
    day = datetime.date.today()
    weekday = day.weekday()
    weekdayToString = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
    tts(f"오늘은 {weekdayToString[weekday]}입니다.")
    return weekdayToString[weekday]