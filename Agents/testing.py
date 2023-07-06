from gtts import gTTS

tts_en = gTTS("hola mi gente como estan?", lang="es")

tts_fr = gTTS("bonjour", lang="fr")


with open("hello_bonjour.wav", "wb") as f:
    tts_en.write_to_fp(f)

    tts_fr.write_to_fp(f)
