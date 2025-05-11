print("number\tsquare\tcube")
for count in range(0, 6):
	square = count * count
	cube = count * count * count
	print(f'{count:>6} {square:>7}{cube:>6}')
	