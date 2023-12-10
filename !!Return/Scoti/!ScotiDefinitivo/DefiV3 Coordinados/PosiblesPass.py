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
    
    
    
     # Verificar si hay un segundo nombre, si no hay usaremos el apellido paterno
    if len(nombres) > 1:
        segundo_nombre = nombres[1].lower().capitalize().strip()
    else:
        
        if len(apellido_paterno) > 1:
            segundo_nombre = apellido_paterno
        else:
            segundo_nombre = 'Peru'

    #separando las fechas de nacimiento
    try:
        fecha_nacimiento = palabras[4].split("/")[2].strip()  # Extraer el año de nacimiento
        fecha_nacimiento_dos_digitos = fecha_nacimiento[-2:]
        dia_nacimiento = palabras[4].split("/")[0].strip()
        mes_nacimiento = palabras[4].split("/")[1].strip()

    except:
        fecha_nacimiento = '1990'
        fecha_nacimiento_dos_digitos = '10'
        dia_nacimiento = '10'
        mes_nacimiento = '10'

    if len(primer_nombre) >= 6:
        print('El nombre tiene mas de 6 caracteres')
        #Por si tiene más de 6 caracteres el nombre
        valor1 = primer_nombre + fecha_nacimiento
        valor2 = primer_nombre + dia_nacimiento
        valor3 = primer_nombre + fecha_nacimiento_dos_digitos
        valor4 =  segundo_nombre + fecha_nacimiento

    if len(primer_nombre) == 4 or len(primer_nombre) == 5:
        print('El nombre tiene 4 o 5 caracteres')

        #Por si tiene más de 6 caracteres el nombre
        valor1 = primer_nombre + fecha_nacimiento
        valor2 = primer_nombre + dia_nacimiento + fecha_nacimiento_dos_digitos
        valor3 = primer_nombre + mes_nacimiento + fecha_nacimiento_dos_digitos
        valor4 =  segundo_nombre + fecha_nacimiento
        
    if len(primer_nombre) <= 3:
        print('El nombre tiene 3 caracteres')
        #Por si tiene más de 6 caracteres el nombre
        valor1 = primer_nombre+ segundo_nombre.lower() + fecha_nacimiento_dos_digitos
        valor2 = primer_nombre + segundo_nombre[0].lower() + fecha_nacimiento
        valor3 = primer_nombre +segundo_nombre[0].lower()  + dia_nacimiento + fecha_nacimiento_dos_digitos 
        valor4 =  segundo_nombre + fecha_nacimiento
    
    # Por si es de 2 digitos o 1 para corregir errores
    valor1 = verificar_y_aumentar_longitud(valor1)
    valor2 = verificar_y_aumentar_longitud(valor2)
    valor3 = verificar_y_aumentar_longitud(valor3)
    valor4 = verificar_y_aumentar_longitud(valor4)
    
    return [numero, valor1, valor2, valor3, valor4]


#Ejemplo de uso:
cadena_entrada = '46786551|LUZ GERARDO|TANTAVILCA|FERNANDEZ|08/01/1991'
#cadena_entrada = '46786550|ANDREA DEL PILAR|YACTAYO|MESTAS|16/03/1991' #correcto
resultado = procesar_cadena(cadena_entrada)
print(resultado)  # Esto imprimirá: ['07542837', 'Gledis1953', 'Gledis1234', 'Reategui1953', 'Montes1953']
