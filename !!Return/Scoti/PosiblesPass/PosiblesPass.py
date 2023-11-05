
with open('data.txt', 'r') as entrada, open('resultado.txt', 'w') as salida:
    for linea in entrada:
        palabras = linea.split()
        
        numero = palabras[0]
        primer_nombre = palabras[1].lower()
        
        fecha_nacimiento = palabras[-1]
        ano_nacimiento = fecha_nacimiento.split('-')[0]

        salida.write(f"{numero} {primer_nombre}{ano_nacimiento}\n")
