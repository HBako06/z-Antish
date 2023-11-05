def verificar_y_aumentar_longitud(valor):
    valores = [4, 5, 6, 7, 8, 9, 10]
    i = 0 
    while len(valor) < 8:
        valor = valor + str(valores[i])
        i = i + 1
    return valor

def procesar_cadena(cadena):
    palabras = cadena.split("|")  # Usamos "|" como separador
    # Extraer los datos
    numero = palabras[0]
    nombres = palabras[1].split()  # Dividir nombres por espacios en blanco
    primer_nombre = nombres[0].lower().capitalize().strip()
    
    # Verificar si hay un segundo nombre
    if len(nombres) > 1:
        segundo_nombre = nombres[1].lower().capitalize().strip()
    else:
        segundo_nombre = ""
    
    apellido_paterno = palabras[2].lower().capitalize().strip()
    fecha_nacimiento = palabras[4].split("/")[2].strip()  # Extraer el año de nacimiento

    valor1 = primer_nombre + fecha_nacimiento
    valor2 = primer_nombre + '1234'
    valor3 = apellido_paterno + fecha_nacimiento
    valor4 = segundo_nombre + fecha_nacimiento

    # Verificar y ajustar la longitud de valor1, valor2, valor3 y valor4 a 8 caracteres
    valor1 = verificar_y_aumentar_longitud(valor1)
    valor2 = verificar_y_aumentar_longitud(valor2)
    valor3 = verificar_y_aumentar_longitud(valor3)
    valor4 = verificar_y_aumentar_longitud(valor4)
    
    # Devolver una lista con los valores
    return [numero, valor1, valor2, valor3, valor4]

    # Ejemplo de uso:
    cadena_entrada = '07542837|GLEDIS|REATEGUI|MONTES|30/04/1953'
    resultado = procesar_cadena(cadena_entrada)
    print(resultado)  # Esto imprimirá: ['07542837', 'Gledis1953', 'Gledis1234', 'Reategui1953', 'Montes1953']
