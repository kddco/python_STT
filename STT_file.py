import speech_recognition as  sr
r = sr.Recognizer()
with sr.AudioFile("F:/training/k2.wav") as source:
    #"C:\Users\Chen\Downloads\english.wav"
     audio = r.record(source)
     try:
        text = r.recognize_google(audio, language='zh-tw')
        print("You said : {}".format(text))
     except:
        print("Sorry could not recognize your voice")
