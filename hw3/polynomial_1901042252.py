def polynomial(x, constants):
	total, temp = 0, 0
	n = len(constants)
	for i in range(len(constants)):
		temp = constants[i]
		for _ in range(n-i-1):
			temp *= x
		total += temp
	return total

x = 4
constants = [7, -3, 5, -9, 27]

print(polynomial(x,constants))
