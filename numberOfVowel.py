def return_sum_of_vowel(name : str)-> int:
	numberOfVowel = 0
	for letters in name:
		if letters == 'a' or letters == 'e' or letters == 'i' or letters == 'o' or letters == 'u' :
			numberOfVowel += 1
	return numberOfVowel


print(return_sum_of_vowel("python is sweet"))