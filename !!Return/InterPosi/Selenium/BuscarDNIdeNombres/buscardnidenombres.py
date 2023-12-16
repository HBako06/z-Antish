
# Parámetros de conexión
import psycopg2

# Parámetros de conexión
conexion_params = {
    "database": "postgres",
    "user": "postgres",
    "password": "abc123$%^",
    "host": "database-1-instance-1.c8dbue4rjz1y.us-east-2.rds.amazonaws.com",
    "port": "5432" 
}


# Conectar a la base de datos
conn = psycopg2.connect(**conexion_params)
cursor = conn.cursor()

# Leer el archivo y ejecutar las consultas
with open('lives.txt', 'r') as file, open('resultados.txt', 'a') as file_output:
    for line in file:
        nombre = line.strip().split(',')[1]
        tarjeta = line.strip().split(',')[0]
        consulta = f"SELECT dni,fecha_nac,nombres,ap_pat,ap_mat FROM personas WHERE nombre_completo LIKE UPPER('%{nombre}%');"
        cursor.execute(consulta)
        resultado = cursor.fetchone()
        
        if resultado:
            # Formatear la línea de salida
            #print(f'test > > >  {resultado}')
            output_line = f"{tarjeta},{resultado[0]},{resultado[1]},{resultado[2]},{resultado[3]},{resultado[4]}"
            # Escribir los resultados en el archivo de salida y en la pantalla
            file_output.write(output_line)
            file_output.write("\n")
            print(output_line)
            #input("Presione Enter para continuar...")
        else:
            # Si no hay resultados, solo escribe la línea original y la imprime
            output_line = f"{tarjeta},None,None,None,None,None"
            file_output.write(output_line + "\n")
            print(output_line)

# Cerrar la conexión
cursor.close()
conn.close()

