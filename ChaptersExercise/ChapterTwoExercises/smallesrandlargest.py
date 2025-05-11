first_number = int(input("Enter the first number: "))
minimum = first_number
maximum = first_number

second_number = int(input("Enter the second number: "))
if(second_number < minimum):
	minimum = second_number
if(second_number > maximum):
	maximum = second_number


third_number = int(input("Enter the third number: "))
if(third_number < minimum):
	minimum = third_number
if(third_number > maximum):
	maximum = third_number

sum = first_number + second_number + third_number
product = first_number * second_number * third_number
average = sum / 3

print(minimum)
print(maximum)
print(sum)

print(product)
print(average)



