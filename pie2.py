number = int(input("Enter a three-digits number:"))

lastNumber = number % 10

twoDigit = number / 10

secondNumber = twoDigit / 10

firstNumber = twoDigit / 10

sum = lastNumber + secondNumber + firstNumber
print("The sum of the three digits is:", sum) 



