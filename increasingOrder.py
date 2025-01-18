first_number = int(input("Enter first number: "))
second_number = int(input("Enter first number: "))
third_number = int(input("Enter first number: "))

smallest = first_number
if second_number < smallest and second_number < third_number:
	smallest = second_number
elif third_number < smallest:
	smallest = third_number 

largest = first_number
if second_number > largest and second_number > third_number:
	largest = second_number
elif third_number > largest:
	largest = third_number

print(smallest, largest)uy
	
