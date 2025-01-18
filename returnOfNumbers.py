def return_sum(numbers) -> int:
	total = 0
	for count in numbers:
		if count.isdigit():
			temp = int(count)
		if temp % 2 == 0:
			total += temp
	return total	



			