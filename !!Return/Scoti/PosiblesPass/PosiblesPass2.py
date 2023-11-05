def verificar_y_aumentar_longitud(valor):
    valores = [4, 5, 6, 7, 8, 9]
    i = 0 
    while len(valor) < 8:
        valor = valor + str(valores[i])
        i = i + 1
    return valor

with open('data.txt', 'r') as entrada, open('resultado.txt', 'w') as salida:
    for linea in entrada:
        palabras = linea.split("|")  # Usamos "|" como separador

        try:
            # Extraer los datos
            numero = palabras[0]
            primer_nombre = palabras[1].split(" ")[1].lower().capitalize().strip()
            apellido_paterno = palabras[2].lower().capitalize().strip()
            fecha_nacimiento = palabras[4].split("/")[2].strip()  # Extraer el año de nacimiento

            valor1 = primer_nombre + fecha_nacimiento
            valor2 = apellido_paterno + fecha_nacimiento

            # Verificar y ajustar la longitud de valor1 y valor2 a 8 caracteres
            valor1 = verificar_y_aumentar_longitud(valor1)
            valor2 = verificar_y_aumentar_longitud(valor2)

            salida.write(f"{numero} {valor1} {valor2}\n")
        except IndexError:
            pass
