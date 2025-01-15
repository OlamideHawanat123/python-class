def get_cube(number):
	return 'invalid data' if type(number) == str else round((number ** 3),3)





def convert_dollar_to_naira(number):
	return 'invalid data' if type(number) == str or number <= 1 else round((number * 1550), 3)
	return 'invalid data' if type(number) != int else round((number * 1550), 3)

	 

			