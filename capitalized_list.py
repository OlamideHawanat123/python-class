def capitalised_list(word)-> list:
	return(list(map(str.capitalize, word)))
	
word = ["ola", "mide", "sugar"]
print(capitalised_list(word))