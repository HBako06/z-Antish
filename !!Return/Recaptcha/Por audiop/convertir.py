from moviepy.editor import *

# Cargar el archivo MP3
audio_clip = AudioFileClip("payload.mp3")

# Convertir a WAV y guardar
audio_clip.write_audiofile("payload.wav")
