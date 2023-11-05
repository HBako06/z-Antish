from PIL import Image
import os

def convertir_a_bn(ruta_carpeta):
    # Lista todos los archivos en la carpeta
    archivos = os.listdir(ruta_carpeta)

    # Filtra los archivos para obtener solo las imágenes
    imagenes = [archivo for archivo in archivos if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # Itera a través de las imágenes y conviértelas a blanco y negro
    for imagen_nombre in imagenes:
        # Ruta completa del archivo de imagen
        ruta_imagen = os.path.join(ruta_carpeta, imagen_nombre)
        
        # Abre la imagen
        imagen = Image.open(ruta_imagen)
        
        # Convierte la imagen en blanco y negro
        imagen_bn = imagen.convert('L')
        
        # Guarda la imagen en blanco y negro
        imagen_bn.save(ruta_imagen)
        
        print(f'La imagen {imagen_nombre} ha sido convertida a blanco y negro en la carpeta {ruta_carpeta}.')

    # Recorre las subcarpetas y aplica la misma operación de forma recursiva
    subcarpetas = [carpeta for carpeta in archivos if os.path.isdir(os.path.join(ruta_carpeta, carpeta))]
    for subcarpeta in subcarpetas:
        convertir_a_bn(os.path.join(ruta_carpeta, subcarpeta))

# Ruta de la carpeta principal que contiene las subcarpetas con letras y sus imágenes
ruta_carpeta_principal = 'Letras'

# Llama a la función para iniciar el proceso de conversión en blanco y negro
convertir_a_bn(ruta_carpeta_principal)

print('Proceso completado.')
