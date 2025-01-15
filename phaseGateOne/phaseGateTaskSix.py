day = int (input("""
Enter today's day:
Sunday = 0
Monday = 1
Tuesday = 2
Wednesday = 3
Thursday = 4
Friday = 5
Saturday = 6
"""))
print(day)
while(day < 0 or day > 7 and type(day) != int):
	day = int(input("Enter valid day: "))

elapsed_day = int(input("Enter the number of days elapsed since today: "))
while(elapsed_day < 0 or elapsed_day > 7 and type(elapsed_day) != int):
	elapsed_day = int(input("Enter  a valid day: "))

match day:
	case 0:
		print("Today is Sunday")

	case 1:
		print("Today is Monday") 

	case 2:
		print("Today is Tuesday") 

	case 3:
		print("Today is Wednesday") 

	case 4:
		print("Today is Thursday") 

	case 5:
		print("Today is Friday") 

	case 6:
		print("Today is Saturday")

elapsed_day += day
for elapsed_day in day:
	print(elapsed_day(day))
 

	




	