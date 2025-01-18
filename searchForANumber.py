def search_for_a_number(number):
	search = int(input("Enter number you want to search for: "))
	number = 0

	for char in str(number):
		if search == char:
			number += 1
	return number 

print(search_for_a_number(2345678))