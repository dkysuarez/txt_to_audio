import pyttsx3
import time

# Initialise the text-to-speech engine
engine = pyttsx3.init(driverName='sapi5')
# Open text file
with open('filepath', 'r', encoding="utf8") as f:
    text = f.read().replace('\n', '')
    f.close()
    engine.say(text)

    # Set volume (0-1)
    engine.setProperty('volume', 1.0)
    # Set speed (words per minute)
    engine.setProperty('rate', 180)
    engine.save_to_file(text, 'audio.mp3')#set location

    engine.runAndWait()
    time.sleep(0.5)


