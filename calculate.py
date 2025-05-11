def calculate_product(*number):
	product = 1
	for count in number:
		product *= count
	return product


print(calculate_product(10, 20, 30))
print(calculate_product(*range(1, 6, 2)))

semi = 'hello'
print(semi.upper())

x = 7
def access():
	global x 
	x = 5
	print("x accessed from local variable :", x)

access()
print(x)
print(id(x))

def exercise(num):
	number = 0
	for count in num:
		number += count ** 2
	return number

number = [1, 2, 3, 4, 5]
print(exercise(number))

def the_hours(number):
	hour i second