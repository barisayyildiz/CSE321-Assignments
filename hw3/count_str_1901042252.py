def countStr(string, start, end):
	counter = 0
	for i in range(len(string)):
		if string[i] == start:
			for j in range(i, len(string)):
				if string[j] == end:
					counter += 1
	return counter

print(countStr("TXZXXJZWX", "X", "Z"))
