integer = int(input("Enter an integer between 0 and 1000"))

third_digit = integer % 10
two_numbers = round(integer / 10)

second_digit = two_numbers % 10
first_digit = round(two_numbers / 10)

print("The sum of all the digits in the user's three-digit number is: ", first_digit + second_digit + third_digit)