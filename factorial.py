def factorial(number):
	factorial = 1
	for count in range(1, number+1):
		factorial *= count
	return factorial


number = 5
print(factorial(number))
		