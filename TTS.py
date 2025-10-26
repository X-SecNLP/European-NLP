from gtts import gTTS
import os

text = "Zu Asche, Zu Staub."

tts = gTTS(text=text, lang='de')

filename = "tts.mp3"
tts.save(filename)

print(f"Saved in {filename}")