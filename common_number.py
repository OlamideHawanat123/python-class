def common_number(number_one,number_two)-> list:
	common = []
	for count in number_one:
		for counter in number_two:
			if count == counter:
				common.append(count)
	return common

number_one = [1, 2, 3]
number_two = [3, 4, 5]
print(common_number(number_one, number_two))