# import speech_recognition as  sr
# import time
# import os
# import pyaudio
# r = sr.Recognizer()  # initialize recognizer初始化
# r.adjust_for_ambient_noise(sr)     # 函數調整麥克風的噪音:
# with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
#     print("Speak Anything :")
#     audio = r.listen(source)  # listen to the source
#     try:
#         text = r.recognize_google(audio, language='zh-tw')  # use recognizer to convert our audio into text part.
#         print("You said : {}".format(text))
#     except:
#         print("Sorry could not recognize your voice")  # In case of voice not recognized  clearly



import speech_recognition as sr

#obtain audio from the microphone
r=sr.Recognizer()
with sr.Microphone() as source:
    print("Please wait. Calibrating microphone...")
    #listen for 5 seconds and create the ambient noise energy level
    r.adjust_for_ambient_noise(source, duration=5)
    print("Say something!")
    audio=r.listen(source)

# recognize speech using Google Speech Recognition
try:
    print("Google Speech Recognition thinks you said:")
    print(r.recognize_google(audio, language="zh-TW"))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("No response from Google Speech Recognition service: {0}".format(e))
