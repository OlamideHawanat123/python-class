words = {}
count = 0
sentence = ("Hawanat was defining a dictionary and kept repeating dict the class had to encourage her to reduce the use of the word dict")
for word in sentence.split():
	if word in words:
		words[word] +=1
	else:
		words[word] = 1
print(words)

wordz = {cls: sentence.split() for cls in sentence}
print(wordz)