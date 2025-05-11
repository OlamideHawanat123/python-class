import random

empty_tuple = ()
empty_tuple = [random.randint(1, 20) for count in range (20)]
print(tuple(empty_tuple))

#print sum of elements at odd position
print(sum(empty_tuple[1::2]))

#print sum of elements at even position
print(sum(empty_tuple[0::2]))

maximum = max(empty_tuple)
minimum = min(empty_tuple)

#print sum of maximum and minimum
total = maximum + minimum
print(total)

#Unpack first five elements and display the product
unpacking = empty_tuple[:5]
product = 1
for counter in unpacking:
    product *=counter
print(product)





set.