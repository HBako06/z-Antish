import pyautogui as p
import time


def procesar_lote():
    linealote = 0
    with open('./dni.txt', 'r') as f:
        lines = f.readlines()

    for line in lines:
        valor1 = line.strip()
        
        # CODIGO MIO . .. .

        time.sleep(0.4)
        p.doubleClick(IngresarNumDocumentoMedio) # para ingresar el numero del documento
        time.sleep(0.1) # esperar un rato para que no se bugee
        p.typewrite(valor1, interval=0.02)
        time.sleep(0.2) 

        registro = open("registro.txt","w")
	    registro.write(valor1.rstrip()) # escribir en el block
	    registro.write("\n")
	    registro.close()
    

if __name__ == "__main__":
    time.sleep(1)
    procesar_lote()
    #borrarDocumento()