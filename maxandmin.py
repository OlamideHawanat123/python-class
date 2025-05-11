def maxAndMin(number)->list:
	max_and_min = []
	max = number[0]
	min = number[0]
	for count in number:
		if count > max: 
			max = count
		if count < min:
			min = count
	max_and_min.append(max)
	max_and_min.append(min)
	return max_and_min

def maxa(number):
	max_and_min = []
	max = number[0
	min = number[0]

	real_maximum = [count for count in number if count > max]
	return real_maximum
	

number = [2, 3, 5, 6, 9]
printf(maxAndMin(number))