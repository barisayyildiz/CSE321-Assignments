class Cheese:
	def __init__(self, weight, price):
		self.weight = weight
		self.price = price
		self.ratio = price/weight
	# used for comparisons
	def __gt__(self, other):
		return self.ratio < other.ratio
	# returns string representation
	def __str__(self):
		return f'[{self.weight},{self.price}]'
	__repr__ = __str__

def insertionSort(arr):
	if len(arr) == 1:
		return arr
	for i in range(1,len(arr)):
		tmp = i
		while arr[tmp] < arr[tmp-1] and tmp > 0:
			arr[tmp], arr[tmp-1] = arr[tmp-1], arr[tmp]
			tmp -= 1
	return arr

# Fractional Knapsack Problem
def knapsack(cheeseArr, cap):
	# sort cheese array by ratio
	cheeseArr = insertionSort(cheeseArr)

	total = 0
	for cheese in cheeseArr:
		# if cheese weight is smaller than the current capacity
		# add all of the cheese to the knapsack
		if cap - cheese.weight >= 0:
			cap -= cheese.weight
			total += cheese.price
		# fill the rest of the capacity with the current cheese
		else:
			fraction = cap / cheese.weight
			total += cheese.price * fraction
			# since no capacity left, return the total value
			return total

# cheese objects
# first param is used for weight, second param is used for price
cheeseArr = [
	Cheese(10,60),
	Cheese(40,40),
	Cheese(20,100),
	Cheese(30,120),
]
cap = 50

print(f'Cheese Array : {cheeseArr}')
print(f'Capacity : {cap}')
print("Maximum value for the knapsack =", knapsack(cheeseArr, cap))
