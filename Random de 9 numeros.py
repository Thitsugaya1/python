#Se importa la funcion randint
from random import randint

#Main code
number = int(raw_input("Enter a number: "))
if (number >= 1):
	print randint(1, number), " - ", randint(1, number), " - ", randint(1, number), " - ", randint(1, number), " - ", randint(1, number), " - ",
	print randint(1, number), " - ", randint(1, number), " - ", randint(1, number), " - ", randint(1, number)
else:
        print "Invalid number"
