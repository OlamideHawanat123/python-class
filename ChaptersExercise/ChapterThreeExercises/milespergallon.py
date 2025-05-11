over_all_miles = 0;
over_all_gallon = 0;

gallon_used = float(input("Enter the gallons used(-1 to terminate) : "))
miles_driven = int(input("Enter the miles driven: "))
miles_per_gallon = miles_driven / gallon_used
print(f' The miles per gallon for this tank was : {miles_per_gallon}')


while gallon_used != -1:
	gallon_used = float(input("Enter the gallons used(-1 to terminate) : "))
	miles_driven = int(input("Enter the miles driven: "))

	miles_per_gallon = miles_driven / gallon_used
	print(f' The miles per gallon for this tank was : {miles_per_gallon:.6f}')

over_all_miles += miles_driven
over_all_gallon += gallon_used

over_all_miles_per_gallon = over_all_miles / over_all_gallon;
print(f' The overall average miles per gallon was : {over_all_miles_per_gallon}')

