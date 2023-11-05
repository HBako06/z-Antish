import cv2
import numpy as np
import tensorflow as tf
from keras.models import load_model
import time
import os
# Load image, grayscale
image = cv2.imread('captcha.png')

# Guardar imágenes redimensionadas en escala de grises
imageOutList = []

for i in range(1, 7):
    imageOut = image[1:60, (i-1)*25+5:i*25+5]
    imageOut = cv2.resize(imageOut, (224, 224))
    imageOut = imageOut / 255.0
    imageOutList.append(imageOut)

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

for i in range(6):
    imagen = imageOutList[i]
    imagen = np.expand_dims(imagen, axis=0)

    start_time = time.time()
    prediccion = predict_image(imagen)
    clase_predicha = class_names[np.argmax(prediccion)]
    confianza = np.max(prediccion)
    elapsed_time = time.time() - start_time
    
    # Mostrar los resultados y el tiempo de ejecución
    print("Clase predicha:", clase_predicha)
    print("Confianza:", str(np.round(confianza * 100, 2)) + "%")
    print("--------------------")

    # Obtiene el último carácter de la clase_predicha y lo concatena a la cadena
    ultimos_caracteres += clase_predicha[-1]

# Imprime la cadena con los últimos caracteres
print("Captcha:", ultimos_caracteres)
os.remove('captcha.png')