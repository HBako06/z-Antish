import cv2
import os
from PIL import Image
import numpy as np
import tensorflow as tf
from keras.models import load_model
import time

# Crea la carpeta de salida si no existe
if not os.path.exists('output'):
    os.makedirs('output')

# Load image, grayscale
image = cv2.imread('captcha.png')

# Recortar y redimensionar la imagen
def resize_and_save(image, output_path):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imagen_redimensionada = Image.new('L', (50, 50), 'white')
    width, height = image_gray.shape[::-1]
    x = (50 - width) // 2
    y = (50 - height) // 2
    imagen_redimensionada.paste(Image.fromarray(image_gray), (x, y))
    imagen_redimensionada.save(output_path)

# Guardar imágenes redimensionadas en escala de grises
for i in range(1, 7):
    ruta_imagen = f"output/imageOut{i}.png"
    imageOut = image[1:60, (i-1)*25+5:i*25+5]
    resize_and_save(imageOut, ruta_imagen)

print("Imágenes procesadas y redimensionadas ")

# Cargar el modelo
model = load_model("keras_Model.h5", compile=False)

# Cargar las clases desde labels.txt
with open("labels.txt", "r") as file:
    class_names = [line.strip() for line in file.readlines()]

# Definir la función de predicción
@tf.function(input_signature=[tf.TensorSpec(shape=[None, 224, 224, 3], dtype=tf.float32)])
def predict_image(image):
    prediction = model(image)
    return prediction

# Inicializa una cadena vacía fuera del bucle
ultimos_caracteres = ""

os.system('cls')

for i in range(1, 7):
    ruta_imagen = f"output/imageOut{i}.png"
    imagen = cv2.imread(ruta_imagen)
    imagen = cv2.resize(imagen, (224, 224))
    imagen = imagen / 255.0
    imagen = np.expand_dims(imagen, axis=0)

    start_time = time.time()
    prediccion = predict_image(imagen)
    clase_predicha = class_names[np.argmax(prediccion)]
    confianza = np.max(prediccion)
    elapsed_time = time.time() - start_time
    # Mostrar los resultados y el tiempo de ejecución

    print(f"Para la imagen {ruta_imagen}:")
    print("Clase predicha:", clase_predicha)
    print("Confianza:", str(np.round(confianza * 100, 2)) + "%")
    print("Tiempo de ejecución:", elapsed_time, "segundos")
    print("--------------------")

    # Obtiene el último carácter de la clase_predicha y lo concatena a la cadena
    ultimos_caracteres += clase_predicha[-1]

# Imprime la cadena con los últimos caracteres
print("Captcha:", ultimos_caracteres)

#os.remove('captcha.png')