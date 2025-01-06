def maximum(numbers):
		largest = numbers[0]
	 	for number in numbers:
			if number > largest:
				largest = number
		return largest

def reverse(integers):
	return integers[::-1]
	

def check(number):
	return 5 in number

def odd(odd_elements):
	index = []
	for count in range (len(odd_elements)):
		if count % 2 == 1:
			index.append(odd_elements[count])
	return index	
def even(even_elements):
	result = []
	for count in range (len(even_elements)):
		if count % 2 == 0:
			result.append(even_elements[count])
	return result

def total(elements):
	total = 0
	for element in elements:
		total += element
	return total 

def sum(list_numbers):
	sum = 0
	for numbers in list_numbers:
		sum += numbers
	return sum

def palindrome(name):
	return name[::-1] == name

def concatenate(list_one, list_two):
	return list_one + list_two

	
def combination(element_one, element_two):
	for element_one in element_two:
		return element_one(len([element_two]))

	
			




