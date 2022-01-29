def cutting(n):
	if n>1:
		return cutting(n/2)+1
	return 0

n = 33
print(f'Minimum number of cutting for {n} is : {cutting(n)}')
