import tkinter as tk
import cv2
import os
from PIL import Image, ImageTk
#import speech_recognition as sr
import libreriatest

class App:
    def __init__(self):
        # Crear la ventana principal
        self.root = tk.Tk()
        self.root.title("Cámara en vivo")

        # Configurar el fondo gris
        self.root.configure(bg='#333333')

        # Configurar el tamaño de la ventana
        self.root.geometry("900x600")

        # Configurar el lienzo para mostrar la imagen de la cámara
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg='#FFFFFF')
        self.canvas.grid(row=0, column=0, padx=10, pady=10, rowspan=3)

        # Configurar la cámara
        self.cap = cv2.VideoCapture(2)

        # Configurar el botón de captura de imagen
        self.button_capture = tk.Button(self.root, text="Capturar imagen", command=self.capture_image)
        self.button_capture.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        # Configurar el botón "inventado"
        self.button_inventado = tk.Button(self.root, text="Botón inventado", command=self.inventado)
        self.button_inventado.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        # Configurar el botón de generar texto
        self.button_texto = tk.Button(self.root, text="Generar texto", command=self.generar_texto)
        self.button_texto.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        # Crear la lista donde se mostrará el texto generado
        self.listbox = tk.Listbox(self.root)
        self.listbox.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

    def capture_image(self):
        # Capturar la imagen de la cámara
        ret, frame = self.cap.read()

        # Guardar la imagen en la carpeta "imagenes"
        if not os.path.exists("imagenes"):
            os.makedirs("imagenes")
        filename = "imagenes/captura.png"
        cv2.imwrite(filename, frame)

    def inventado(self):
        # Método inventado al presionar el segundo botón
        print("Se presionó el botón inventado")

    def generar_texto(self):
        # Generar el texto "Hola mundo"
        self.listbox.insert(tk.END, "Hola mundo")

    def run(self):
        # Función principal para ejecutar la aplicación
        while True:
            # Capturar la imagen de la cámara
            ret, frame = self.cap.read()

            # Convertir la imagen a formato adecuado para Tkinter
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img_tk = tk.PhotoImage(data=cv2.imencode('.png', img)[1].tobytes())

            # Actualizar la imagen en el lienzo
            self.canvas.delete("all")
            image_item = self.canvas.create_image(0, 0, anchor="nw", image=img_tk)
            self.canvas.itemconfig(image_item, image=img_tk)

            # Esperar 10 milisegundos antes de actualizar la imagen
            self.root.update_idletasks()
            self.root.update()
            cv2.waitKey(10)

if __name__ == '__main__':
    app = App()
    app.run()
