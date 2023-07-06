import pyttsx3
import subprocess
import os
import wave

# Step 1: Install necessary libraries if not already installed
# pip install pyttsx3


def get_wav_duration(file_path):
    with wave.open(file_path, "rb") as wav_file:
        frames = wav_file.getnframes()
        rate = wav_file.getframerate()
        duration = frames / float(rate)
        return round(duration, 1)


# Step 2: Initialize the pyttsx3 engine
def playNarrator(text, rate=150):
    # Init and set properties
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    # Select the first voice in the list
    engine.setProperty("voice", voices[29].id)
    engine.setProperty("rate", rate)  # Set the speaking rate in words per minute

    # Step 2: Generate the narrator voice
    engine.save_to_file(text, "narration.wav")
    engine.runAndWait()

    with open(os.devnull, "w") as devnull:
        subprocess.call(
            [
                "ffmpeg",
                "-i",
                "narration.wav",
                "-acodec",
                "pcm_s16le",
                "-ac",
                "1",
                "-ar",
                "16000",
                "out.wav",
                "-y",
            ],
            stdout=devnull,
            stderr=devnull,
        )

    # Step 3: Get the duration of the audio file
    file_path = "out.wav"
    duration = get_wav_duration(file_path)
    print(f"Duration of the audio: {duration} seconds")

    # Step 4: Use ffmpeg to play the audio !!!!!!!!!!!!!!!
    # Requiere tener ffmpeg instalado en el sistema y anadido al PATH como variable de entorno
    # with para que no se muestre el output de ffplay en la consola y generemos logs de mas (Se puede quitar para debug)
    with open(os.devnull, "w") as devnull:
        subprocess.call(
            ["ffplay", "-nodisp", "-autoexit", "out.wav"],
            stdout=devnull,
            stderr=devnull,
        )

    # Step 5: Delete the audio fileeeee after playing
    os.remove("narration.wav")
    os.remove("out.wav")


playNarrator(
    """
    Hola como estas? El dia de hoy te voy a contar una historia muy interesante. La primera escena es...
"""
)
