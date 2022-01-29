class Candy:
	def __init__(self, length, price):
		self.length = length
		self.price = price
	# used for comparisons
	def __lt__(self, other):
		return self.price < other.price
	# returns string representation
	def __str__(self):
		return f'[{self.length},{self.price}]'
	__repr__ = __str__

# 0/1 Knapsack Problem
def knapsack(candies, cap):
	# it generates a DP table filled with 0's
	table = [[0 for _ in range(cap+1)] for _ in range(len(candies)+1)]

	for i in range(len(candies)+1):
		for l in range(cap+1):
			if i == 0 or l == 0:
				continue
			elif candies[i-1].length <= l:
				# compare the value with the previous row's value
				table[i][l] = max(candies[i-1].price + table[i-1][l-candies[i-1].length],
													table[i-1][l])
			else:
				table[i][l] = table[i-1][l]
	
	# return the max value
	return table[len(candies)][cap]

# candy objects
# first param is length, second param is value
candies = [
	Candy(1,1),
	Candy(2,5),
	Candy(3,8),
	Candy(4,9),
	Candy(5,10),
	Candy(6,17),
	Candy(7,17),
	Candy(8,20),
]
cap = 8
print(f'Candies : {candies}')
print(f'Capacity : {cap}')
print("Maximum value for the knapsack =", knapsack(candies, cap))

