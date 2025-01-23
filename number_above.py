def number_above_seventy_Five(number : list)-> list:
	return ([count for count in number if count >= 75 and count <= 100])
	

number = [12, 45, 3, 75, 100, 500]
print(number_above_seventy_Five(number))