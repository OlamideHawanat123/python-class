division =  [45, 6, 87]
maximum = division[0]
minimum = division[0]
normal_number = 0

for cheese in division:
	if cheese > maximum:
		maximum = cheese
	if cheese < minimum:
		minimum = cheese
	if cheese != maximum or cheese != minimum:
		normal_number = cheese
print(maximum, minimum, normal_number)