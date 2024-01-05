import speech_recognition as sr
from moviepy.editor import *

def audioATexto(audioURL):
    # Convertir MP3 a WAV
    audio_clip = AudioFileClip(audioURL)
    audio_clip.write_audiofile("captcha_audio.wav")

    # Inicializar el reconocedor
    r = sr.Recognizer()

    # Leer y transcribir el archivo WAV
    try:
        with sr.AudioFile('captcha_audio.wav') as source:
            audio = r.record(source)  # Leer el archivo completo
        #print("Texto: " + r.recognize_google(audio, language='en-EN'))
        p = r.recognize_google(audio, language='es-ES')
        # Borrar los archivos MP3 y WAV
        
        print('texto: ' + p)
        #print(type(p))
        return str(p)
        
    except :
        print("No se pudo completar la solicitud a Google Web Speech API")
        
    # Borrar los archivos MP3 y WAV
    
    return "Error"

