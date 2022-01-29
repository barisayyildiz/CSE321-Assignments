def exp_bf(a, n):
	if n == 0:
		return 1
	return a*exp_bf(a, n-1)

def exp_dac(a, n):
	if n == 0:
		return 1
	result = exp_dac(a,n//2)
	if n % 2 == 0:
		return result*result
	else:
		return a*result*result

a, n = 2, 10
print(f'{a}^{n} : {exp_bf(a,n)}')
print(f'{a}^{n} : {exp_dac(a,n)}')
