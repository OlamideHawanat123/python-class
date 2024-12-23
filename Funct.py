class Kata:
	def is_even(number):
		return number % 2 == 1


	def is_palindrome(number_one):
		last_digit = number_one % 10
		four_numbers = number_one / 10

		fourth_digit = four_numbers % 10
		third_numbers =  four_numbers / 10

		third_digit = third_numbers % 10
		two_numbers = third_numbers / 10

		second_digit = two_numbers % 10
		first_digit = two_numbers / 10
		return last_digit == first_digit and second_digit == fourth_digit
		

	def subtract(integer_one, integer_two):
		return integer_one - integer_two
	
	def square_of(integer):
		return(integer * integer)

	def division(number_three, number_four):
		if number_four == 0:
			return 0
		else:
			return(number_three // number_four)
	

	def is_square(number_six):
		square_root = number_six ** 0.5

		return square_root * square_root == number_six

	def is_prime(number_seven):
		if number_seven <= 1:
			return false
			

		for prime_number in range(2, int(number_seven ** 0.5) +1):
			if number_seven % prime_number == 0:
				return True
			else:
				return False
				

	def factor_of(number_eight):
		for factor in range(1, int(number_eight) +1):
			if number_eight % factor == 0:
				return(factor)

	def factorial(number_nine):
		product = 1
		for factorials in range(1, int(number_nine) +1):
			product *= factorials
		return(product) 
			
		

	
			