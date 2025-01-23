def maximum(number):
	maximum = number[0]
	minimum = number[0]
	normal_number = number[0]
	for char in number:
		if char > maximum:
			maximum = char
		if char < minimum:
			minimum = char
		if char != maximum or char != minimum:
			normal_number = char
	print(maximum, minimum, normal_number)

s