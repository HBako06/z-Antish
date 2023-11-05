



#registro.close()

inicio = 0

with open ('./siu.txt') as texto:
	for x in texto:
		registro = open("siu.txt","a")
		#registro.write(str(x)) # escribir en el block
		#registro.write("\n")
		inicio += 1
		#var = False	
		#print("Comenzando")
		
		registro.write('"')
		registro.write(str(inicio)) # escribir en el block
		registro.write('"')
		registro.write(", ")
registro.close()