#Function to calculate the fibonacci serie
def Fibonacci(numb):
	corrent = 1
	lasted = 0
	for i in range (numb):
		print corrent
		corrent += lasted
		lasted = corrent - lasted

#main program
number = int(raw_input("Cantidad de numeros de la secuencia de fibonacci: "))
Fibonacci(number)
