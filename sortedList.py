def sorted_list(number_one, number_two):
	concatenated_list = number_one + number_two
	sorted_list = []
	for count in concatenated_list:
		sorted_list.append(count < count +1) 


number_one = [1, 2, 3, 4]
number_two = [2, 3, 6]
print(sorted_list(number_one, number_two))