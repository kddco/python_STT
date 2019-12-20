import speech_recognition as  sr

r = sr.Recognizer()  # initialize recognizer初始化
with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
    print("Speak Anything :")
    audio = r.listen(source)  # listen to the source
    try:
        text = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize your voice")  # In case of voice not recognized  clearly

'''
r = speech_recognition.Recognizer()
with speech_recognition.AudioFile("C:/Users/user/Desktop/kxt41-w0o3s.wav") as source:
     audio = r.record(source)
     try:
        text = r.recognize_google(audio, language='zh-tw')
        print("You said : {}".format(text))
     except:
        print("Sorry could not recognize your voice")
'''