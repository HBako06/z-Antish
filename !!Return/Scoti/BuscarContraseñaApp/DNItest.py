
dni = '06163519'
iteraciones = 100

for _ in range(iteraciones):
    print(dni)

    dni = str(int(dni) + 1).zfill(8)
