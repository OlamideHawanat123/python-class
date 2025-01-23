def return_prime(number):
	counter = 0
	for count in range(1, number+1):
		if number % count == 0:
			counter += 1
	if counter == 2:
		return True
	else:
		return False


print(return_p  rime(19))
