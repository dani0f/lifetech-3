from gtts import gTTS
import os
import sounddevice as sd
import soundfile as sf


def generate_audios(texts):
    filenames = []
    for i, text in enumerate(texts):
        if(len(text) > 0 ):
            print(text)
            filename = f"audio_{i}.mp3"
            tts = gTTS(text, lang='es')
            tts.save(filename)
            filenames.append(filename)
    return filenames

def play_audio(filename):
    data, fs = sf.read(filename)
    sd.play(data, fs)
    sd.wait()
    os.remove(filename)


