import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices: 
    engine.setProperty('voice', voices[-2].id)

engine.say("Olá Sr. Fernando eu sou a sua assistente virtual IAminuelle, quer que eu ligue para a Sr.Isabele?")
engine.runAndWait()