import os

def CambiarProyecto(archivo):
	archivo = str(archivo)
	arduino_path = "C:/Users/henry/AppData/Local/Arduino15" # Ruta a la carpeta de instalación de arduino-cli
	board_type = "arduino:avr:uno" # Tipo de placa de Arduino que estás utilizando
	port = "COM3" # Puerto serial al que está conectada la placa de Arduino
	sketch_path = f"C:\\Users\\henry\\OneDrive\\Documentos\\Arduino\\{archivo}\\{archivo}.ino" # Ruta al archivo de tu sketch

	os.system(f"{arduino_path}/arduino-cli compile --fqbn {board_type} {sketch_path}")
	os.system(f"{arduino_path}/arduino-cli upload -p {port} --fqbn {board_type} {sketch_path}")


CambiarProyecto("holaMundo")