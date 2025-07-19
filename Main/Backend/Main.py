from gtts import gTTS
from playsound import playsound
import os
import tempfile

def text_to_speech(text, lang='en'):
    # Generate a temporary file path
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tts = gTTS(text=text, lang=lang)
        tts.save(tmp_file.name)
        audio_path = tmp_file.name

    try:
        playsound(audio_path)
    finally:
        # Delete the file after playing
        if os.path.exists(audio_path):
            os.remove(audio_path)
            print("Audio file deleted.")

if __name__ == "__main__":
    user_text = input("Enter text to convert to speech: ")
    text_to_speech(user_text)
