from gtts import gTTS   #Supports text to speech and replay
import os

#Input text
mytext = "Welcome to this program!"

#Language selection
language = "en"

#CORE: Converts text to speech to audio language.
myObj = gTTS(text = mytext, lang = language, slow =False)


#Saves and plays mp.3
myObj.save("welcome.mp3")

os.system("start welcome.mp3")