import speech_recognition as sr
import pyttsx3

def stt():
  r = sr.Recognizer()
  with sr.Microphone() as source:
      r.pause_threshold = 0.8
      print("Say something!")
      audio = r.listen(source)
      said = r.recognize_google(audio, language="ko-KR")
      print("You said: " + said)
      print("Done!")
      return said

def tts(msg):
    engine = pyttsx3.init()
    engine.say(msg)
    engine.runAndWait()