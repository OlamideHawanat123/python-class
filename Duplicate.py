def duplicate(number):
	condition = True
	for count in number:
		if count in number == count:
			condition = True
		else:
			condition = False
	return condition
		

number = [1, 2, 3, 5, 2]
print(duplicate(number))