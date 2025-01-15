def maximum(numbers):
	largest = numbers[0]
	for count in numbers:
		if count > largest:
			largest = count
	return largest    