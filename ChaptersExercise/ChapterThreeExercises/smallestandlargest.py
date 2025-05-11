total = 0
product = 1
numbers_list = []
for count in range(4):
	numbers = int(input("Enter number: "))
	total += numbers
	average = total / 4
	product *= numbers
	numbers_list.append(numbers)
	maximum = max(numbers_list)
	minimum = min(numbers_list)
print(f'Maximum:{maximum} Minimum:{minimum} Sum:{total} Product:{product}Average:{average}')
