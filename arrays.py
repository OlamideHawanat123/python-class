def maximum(numbers):
	largest = numbers[0]
	for count in numbers:
		if count > largest:
			largest = count
	return largest 

def minimum(numbers):
	smallest = numbers[1]
	for count in numbers:
		if count < smallest:
			smallest = count
	return smallest

def summation(numbers):
	sum = 0
	for count in numbers:
		sum += count
	return sum

def sum_even(integers):
	sum = 0
	for count in integers:
		if count % 2 == 0:
			sum += count
	return sum

def sum_odd(numbers):
	sum = 0
	for count in numbers:
		if count % 2 == 1:
			sum += count
	return sum

def max_min(numbers):
	largest = numbers[0]
	smallest = numbers[0]
	for count in numbers:
		if count > largest:
			largest = count
	for count in numbers :
		if count < smallest:
			smallest = count
	return ([largest, smallest])
	 
def odd_integers(numbers):
	counter = 0
	for count in numbers:
		if count % 2 == 1:
			counter += 1
	return counter

def even_integers(numbers):
	counter = 0
	for count in numbers:
		if count % 2 == 0:
			counter += 1
	return counter

def even_numbers(integers):
	even_numbers = []
	for num in integers:
		if num % 2 == 0:
			even_numbers.append(num)
	return even_numbers  

def odd_numbers(integers):
	odd_numbers = []
	for count in integers:
		if count % 2 == 1:
			odd_numbers.append(count)
	return odd_numbers

def squared_numbers(numbers):
	square = []
	for count in numbers:
		square.append(count * count)
	return square

