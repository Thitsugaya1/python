def printNumberDiagonal(number):
	n = number
	i = 0
	while i < number:
		j = 0
		while j < number:
			if i == j:
				print n,
				n -= 1
			else:
				print "*",
			j += 1
		print ""
		i += 1

def printMatrixNx2(number):
	while number > 0:
		if number%2 == 0:
			print "*", number
		else:
			print number, "*"
		number-=1
			

#main code
number=int(raw_input("input a number: "))
printNumberDiagonal(number)
print ""
printMatrixNx2(number)
