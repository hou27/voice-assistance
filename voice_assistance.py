import pyttsx3
import webbrowser

from stt_tts import tts, stt
from get_info import get_time, get_day


def assistance():
    tts('''안녕하세요 voice assistance입니다.
    종료를 원하시면 종료라고 말씀해주세요.
    무엇을 도와드릴까요?''')
    engine = pyttsx3.init()
    for voice in engine.getProperty('voices'):
        if "KO" in voice.id:
            print(voice.id,"로 음성 엔진이 설정되었습니다.")
            engine.setProperty('voice', voice.id)
    while True:
        said = stt()
        if "시간" in said:
            get_time()
        elif "날짜" in said:
            get_day()
        elif "유튜브" in said:
            tts("유튜브를 여는 중 입니다.")
            webbrowser.open("https://www.youtube.com")
        elif "종료" in said:
            tts("안녕히가세요.")
            break
        else:
            tts("알 수 없는 명령어입니다. 다시 말씀해주세요.")


if __name__ == '__main__':
    assistance()