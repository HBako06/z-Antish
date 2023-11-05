import re

# Abrir y leer el contenido de los archivos
with open('resultadoHuella.txt', 'r') as file:
    resultado_data = file.readlines()

with open('resultadoZeeker.txt', 'r') as file:
    resultados_zeeker_data = file.readlines()

# Crear un diccionario para almacenar la información de huellas de resultado.txt
huellas_dict = {}
# Expresión regular para extraer DNI y datos de huellas
pattern = r'DNI: (\d+).*?(Índice: \d+|Pulgar: \d+)'

for line in resultado_data:
    match = re.search(pattern, line)
    if match:
        # Almacenar la información de huellas usando DNI como clave
        huellas_dict[match.group(1)] = match.group(2)

# Función para actualizar la línea con la información de huellas
def actualizar_linea_con_huellas(line, dni, huella_info):
    if f'DNI: {dni}' in line:
        # Añadir la información de huella a la línea
        return line.strip() + ' - ' + huella_info + '\n'
    return line

# Actualizar ResultadosZeeker.txt con la información de huellas de resultado.txt
resultados_zeeker_actualizado = [
    actualizar_linea_con_huellas(line, dni, huella_info)
    for dni, huella_info in huellas_dict.items()
    for line in resultados_zeeker_data
    if f'DNI: {dni}' in line
]

# Escribir los datos actualizados en un nuevo archivo
with open('ResultadosZeeker_Merged.txt', 'w') as file:
    file.writelines(resultados_zeeker_actualizado)
