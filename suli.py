def largest (numbers):
	largest = numbers[0]
	for count in numbers:
		if count > largest:
			largest = count
		return largest
	
numbers = int(input("length: "))
list = []
for counter in range (numbers):
	elements = int(input ("enter the elements:"))
list.append(elements)
print(list)

largest_result = largest(numbers)
print (largest_result)