def sum_of_product(number : list)-> list:
	sum_of_product = 0
	for count in number:
		sum_of_product += count * count
	return sum_of_product

number = [1, 2, 3, 4]
print(sum_of_product(number))