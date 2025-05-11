number = int(input("Enter a five digits number: "))

fifth_number = number % 10
four_numbers = number // 10

fourth_number = four_numbers % 10
three_numbers = four_numbers // 10

third_number = three_numbers % 10
two_numbers = three_numbers //  10

second_number = two_numbers % 10
first_number = two_numbers // 10

print(first_number, second_number, third_number, fourth_number, fifth_number, " ")