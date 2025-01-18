def add_integers(number):
	total = 0
	for count in str(number):
		total += int(count)
	return total


print(add_integers(72349))