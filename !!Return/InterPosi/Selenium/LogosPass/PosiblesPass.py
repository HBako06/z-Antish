def verificar_y_aumentar_longitud(valor):
    valores = [0, 1, 2, 3, 4, 5, 6]
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
    
    apellido_paterno = palabras[2].lower().capitalize().strip()
    apellido_paterno =apellido_paterno.split()
    apellido_paterno = apellido_paterno[0]
    
     # Verificar si hay un segundo nombre
    if len(nombres) > 1:
        segundo_nombre = nombres[1].lower().capitalize().strip()
    else:
        
        if len(apellido_paterno) > 1:
            segundo_nombre = apellido_paterno
        else:
            segundo_nombre = 'Peru'

    try:
        fecha_nacimiento = palabras[4].split("/")[2].strip()  # Extraer el año de nacimiento
        fecha_nacimiento_dos_digitos = fecha_nacimiento[-2:]
        dia_nacimiento = palabras[4].split("/")[0].strip()
    except:
        fecha_nacimiento = '1990'
        fecha_nacimiento_dos_digitos = '10'
        dia_nacimiento = '10'

    valor1 = primer_nombre + fecha_nacimiento
    valor2 = primer_nombre + dia_nacimiento
    valor3 = primer_nombre + fecha_nacimiento_dos_digitos
    valor4 =  segundo_nombre + fecha_nacimiento

    # Verificar y ajustar la longitud de valor1, valor2, valor3 y valor4 a 8 caracteres
    valor1 = verificar_y_aumentar_longitud(valor1)
    valor2 = verificar_y_aumentar_longitud(valor2)
    valor3 = verificar_y_aumentar_longitud(valor3)
    valor4 = verificar_y_aumentar_longitud(valor4)
    
    # Devolver una lista con los valores
    #return [numero, valor1, valor4]
    return [numero, valor1, valor2, valor3, valor4]

    #Ejemplo de uso:
    cadena_entrada = '07570076|ANDRES|MACCHIAVELLO|VASQUEZ|None'
    resultado = procesar_cadena(cadena_entrada)
    print(resultado)  # Esto imprimirá: ['07542837', 'Gledis1953', 'Gledis1234', 'Reategui1953', 'Montes1953']

def procesar_cadena_Interbank(cadena):
    ##4110930625861841,07316480,06/04/1959,ELIZABETH CLOTILDE,GARCIA,CAMARGO
    
    palabras = cadena.split(",")  
    # Extraer los datos
    nombres = palabras[3].split()  # Dividir nombres por espacios en blanco
    primer_nombre = nombres[0].lower().capitalize().strip()
    
    apellido_paterno = palabras[4].lower().capitalize().strip()
    apellido_paterno =apellido_paterno.split()
    apellido_paterno = apellido_paterno[0]
    
     # Verificar si hay un segundo nombre
    if len(nombres) > 1:
        segundo_nombre = nombres[1].lower().capitalize().strip()
    else:
        
        if len(apellido_paterno) > 1:
            segundo_nombre = apellido_paterno
        else:
            segundo_nombre = 'Peru'

    try:
        fecha_nacimiento = palabras[2].split("/")[2].strip()  # Extraer el año de nacimiento
        fecha_nacimiento_dos_digitos = fecha_nacimiento[-2:]
        dia_nacimiento = palabras[2].split("/")[0].strip()
    except:
        fecha_nacimiento = '1990'
        fecha_nacimiento_dos_digitos = '10'
        dia_nacimiento = '10'

    valor1 = primer_nombre + fecha_nacimiento
    valor2 = primer_nombre + dia_nacimiento
    valor3 = primer_nombre + fecha_nacimiento_dos_digitos
    valor4 =  segundo_nombre + fecha_nacimiento

    # Verificar y ajustar la longitud de valor1, valor2, valor3 y valor4 a 8 caracteres
    valor1 = verificar_y_aumentar_longitud(valor1)
    valor2 = verificar_y_aumentar_longitud(valor2)
    valor3 = verificar_y_aumentar_longitud(valor3)
    valor4 = verificar_y_aumentar_longitud(valor4)
    
    # Devolver una lista con los valores
    #return [numero, valor1, valor4]
    return [valor1, valor2, valor3, valor4]

#print(procesar_cadena_Interbank('4110930625861841,07316480,06/04/1959,ELIZABETH CLOTILDE,GARCIA,CAMARGO'))