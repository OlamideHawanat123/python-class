def farenheit(args):
	faren = (9/5) * args + 32
	return faren

for celcius in range (0, 100):
	number = farenheit(celcius)
print(f' CELCIUS {celcius}, FARENHEIT {number}')
