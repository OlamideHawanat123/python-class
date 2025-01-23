def addition(number):
	#total = 0
	#for count in number:
	#	if count % 2 == 0:
	#		total += count

	#return total
	return sum([count for count in number if count % 2 == 0])
	 
	
number = [2, 7, 5, 11, 7, 19, 2, 8, 10]
print(addition(number))