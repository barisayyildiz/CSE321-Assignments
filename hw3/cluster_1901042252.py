def bruteForce(regions):
	maximum = float('-inf')
	start, end = None, None
	cluster = "("
	for i in range(len(regions)):
		total = 0
		for j in range(i, len(regions)):
			total += regions[j]["value"]
			if total > maximum:
				maximum = total
				start, end = regions[i]["id"], regions[j]["id"]
	passed = False
	for rg in regions:
		if rg["id"] != start and (not passed):
			continue
		passed = True
		cluster += f'{rg["id"]}-'
		if rg["id"] == end:
			break
	cluster += "\b)"
	return cluster


def crossSum(arr):
	mid = len(arr) // 2
	sm = 0
	leftSum = float('-inf')
	rightSum = float('-inf')

	for i in range(mid-1, -1, -1):
		sm += arr[i]["value"]
		if sm > leftSum:
			leftSum = sm
	sm = 0
	for i in range(mid, len(arr)):
		sm += arr[i]["value"]
		if sm > rightSum:
			rightSum = sm
	return max(leftSum, rightSum, leftSum+rightSum)

def divideAndConquer(arr):
	if len(arr) == 1:
		return arr[0]["value"]
	
	mid = len(arr) // 2
	leftArr = arr[0:mid]
	rightArr = arr[mid:]

	ls = divideAndConquer(leftArr)
	rs = divideAndConquer(rightArr)
	return max(ls, rs, crossSum(arr))

regions = [
	{
		"id" : "A",
		"value" : 3
	},
	{
		"id" : "B",
		"value" : -5
	},
	{
		"id" : "C",
		"value" : 2
	},
	{
		"id" : "D",
		"value" : 11
	},
	{
		"id" : "E",
		"value" : -8
	},
	{
		"id" : "F",
		"value" : 9
	},
	{
		"id" : "G",
		"value" : -5
	}
]

print(bruteForce(regions))
print(divideAndConquer(regions))
