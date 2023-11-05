import random, string, itertools, argparse
class Generate():

	"""
	Documentacion de Texto:

	Para utilizar el metodo generate('NumAndString', int(cantity), 'method') de la clase
	Generate() se debe seguir los siguientes pasos:

	>>> generador = Generate()
	>>> respuesta  = generador.generate('NumAndString', int(cantity), 'method' )
	>>> print(respuesta)

	NOTA:
		La respuesta sera:
			- En caso Correcto:
				- ({'state':'Ok', 'cantity':'longitud_argumento'}, ['elemento'])

			- En caso de Errores;
				- ({'state':'name_error', 'cantity':'Fail'}, None)

	Argumentos:
		1ero: 
			- Utilize:
				- $: Para numeros en el rango del 0 al 9.
				- *: Para letras en el rango de la 'a-z' sin tildes.

		2do: 
			- Representa las veces a generar.

		3ero: 
			- En caso de usar letras (Solo las que se generan):
				- upper: Mayuscula
				- lower: Minuscula
	"""

	def generate(self, NumAndString, cantity, method):
		
		verifiy = NumAndString

		try:

			letters = string.ascii_lowercase
			for x in range(2): NumAndString = NumAndString[::-1]+'"'

			NumAndString = NumAndString.replace("$", r"{random.randint(0,9)}").replace("*", r"{random.choice(letters).method()}".replace('method', method))
			
			data = []		
			for x in range(cantity): data.append(eval('f'+NumAndString))
			
			data = list(set(data))

			verifiy = ({'state':'Ok', 'cantity':len(verifiy)}, data)

		except Exception as error:
			verifiy = ({'state':type(error).__name__, 'cantity':'Fail'}, None)

		return verifiy

	def luhn_mod10(self, Card):
		tarjeta = map(int, Card)
		tarjeta = list(tarjeta)
		multiplicar = [tarjeta[x] for x in range(0,16,2)]

		for x in range(len(multiplicar)):
			multiplicar[x]*=2
			if len(str(multiplicar[x])) == 2:	multiplicar[x] = eval('+'.join(str(multiplicar[x])))

		isLuhnS = []
		for x in range(1,16,2): isLuhnS.append(tarjeta[x])
		check = (sum(multiplicar)+sum(isLuhnS)) % 10
		
		if check == 0: return True

	def dni_gen(self, last):
		lista = list(itertools.product('0123456789', repeat=6))
		dnis = []
		for x in range(len(lista)):
			texto = ''
			for m in range(len(lista[x])):
				texto += lista[x][m]

			dnis.append(texto+str(last)+'\n')

		with open('dnis.txt', 'w') as my_dnis:
			my_dnis.writelines(dnis)

		return True

	def permutate(self, content, repeat):
		lista = list(itertools.product(content, repeat = repeat))
		permutation = []
		for x in range(len(lista)):
			texto = ''
			for m in range(len(lista[x])):
				texto += lista[x][m]

			permutation.append(texto+'\n')

		return permutation

def generate_bins(bin_number, times):
		bin_number = bin_number.replace('x','$')
		gen = Generate()
		if bin_number.count('$') <= 3: veces = 100
		else: veces = 30

		gen = gen.generate(bin_number, times*veces, 'lower')
		gen = gen[1]
		bins_luhn = []


		for x in range(len(gen)):
			gent = Generate()
			if gent.luhn_mod10(gen[x]): bins_luhn.append(gen[x])

		bins1 = []
		for x in range(times):
			try: bins1.append(bins_luhn[x])
			except: pass
		
		return bins1
