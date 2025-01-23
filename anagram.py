def anagram(name_One, name_Two)-> bool:
	for count in name_One:
		if count in name_Two:
			return True
		else:
			return False
x = "silent"
y = "listpn"
print(anagram(x, y ))