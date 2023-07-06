import pyttsx3
import subprocess
from pydub import AudioSegment
import os

# Step 1: Install necessary libraries if not already installed
# pip install pyttsx3 pydub

# Step 2: Initialize the pyttsx3 engine
def playNarrator(text, rate=150):
    # Init and set properties
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')  # Select the first voice in the list
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', rate) # Set the speaking rate in words per minute

    # Step 2: Generate the narrator voice
    engine.save_to_file(text, 'narration.wav')
    engine.runAndWait()

    # Step 3: Get the duration of the audio file
    audio = AudioSegment.from_wav('narration.wav')
    duration = round(audio.duration_seconds, 1)
    print(f"Duration of the audio: {duration} seconds")

    # Step 4: Use ffmpeg to play the audio !!!!!!!!!!!!!!!
    # Requiere tener ffmpeg instalado en el sistema y anadido al PATH como variable de entorno
    # with para que no se muestre el output de ffplay en la consola y generemos logs de mas (Se puede quitar para debug)
    with open(os.devnull, 'w') as devnull:
        subprocess.call(['ffplay', '-nodisp', '-autoexit', 'narration.wav'], stdout=devnull, stderr=devnull)

    # Step 5: Delete the audio fileeeee after playing
    os.remove('narration.wav')

playNarrator("""
    Diapositiva 1: Información y RequisitosEn esta diapositiva, nos centraremos en obtener información sobre la Sociedad Mutual
    y verificar los requisitos de afiliación. Esto puede incluir detalles como la edad mínima, ubicación geográfica y cuotas de ingreso o periódicas.
    Es importante familiarizarse con estos requisitos antes de proceder.
""")
