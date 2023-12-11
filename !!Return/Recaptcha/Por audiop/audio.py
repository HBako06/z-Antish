import speech_recognition as sr
from moviepy.editor import *
import os

# Convertir MP3 a WAV
audio_clip = AudioFileClip("captcha_audio.mp3")
audio_clip.write_audiofile("captcha_audio.wav")

# Inicializar el reconocedor
r = sr.Recognizer()

# Leer y transcribir el archivo WAV
try:
    with sr.AudioFile('captcha_audio.wav') as source:
        audio = r.record(source)  # Leer el archivo completo
    #print("Texto: " + r.recognize_google(audio, language='en-EN'))
    print("Texto: " + r.recognize_google(audio, language='es-ES'))
except sr.UnknownValueError:
    print("Google Web Speech API no pudo entender el audio")
except sr.RequestError as e:
    print(f"No se pudo solicitar resultados de Google Web Speech API; {e}")

# Borrar los archivos MP3 y WAV
os.remove("captcha_audio.mp3")
os.remove("captcha_audio.wav")
