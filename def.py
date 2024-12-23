def maximum(numbers):
	largest = numbers[0]
	for number in numbers:
		if number > largest:
			largest = number
	return largest
numbers = [34, 78, 12, 45]
largest_result = maximum(numbers)
print(largest_result)



