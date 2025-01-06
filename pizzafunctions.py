from pizza import pizza_types
types = {}

types["Sapa size"] = {"Slice" :4, "Price" : 2500}
types["Small money"] = {"Slice" :6, "Price" : 2900}
types["Big boys"] = {"Slice" :8, "Price" : 4900}
types["Odogwu"] = {"Slice" :12, "Price" : 5200}


print(types)
choice = (input("Choose your preferred option from these available types:"))
for number in types:
	if choice(number) == 1:
		print("yo")

