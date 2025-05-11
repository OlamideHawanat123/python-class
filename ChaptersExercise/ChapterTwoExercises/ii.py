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
passes = 0
fail = 0

for count in range(10):
	result = int(input("Enter result(1 = pass, 2 = fail): "))
	if result == 1:
		passes += 1
	elif result == 2:
		fail += 1

print(f' Passed:{passes}')
print(f' Failed:{fail}')

if(passes >= 8):
	print("Bonus to the instructor")