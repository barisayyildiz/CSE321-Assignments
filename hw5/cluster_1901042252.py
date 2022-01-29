def maxProfit(arr):
	maxSum, tmp = arr[0], arr[0]
	for i in range(1, len(arr)):
		tmp = max(arr[i], tmp+arr[i])
		maxSum = max(maxSum, tmp)
	return maxSum

arr = [3,-5,2,11,-8,9,-5]
print(f"Maximum profit is : {maxProfit(arr)}")


# # ============= HOMEWORK 3 =================
# # Question 5.b, Divide and Conquer Approach

# def crossSum(arr):
# 	mid = len(arr) // 2
# 	sm = 0
# 	leftSum = float('-inf')
# 	rightSum = float('-inf')

# 	for i in range(mid-1, -1, -1):
# 		sm += arr[i]["value"]
# 		if sm > leftSum:
# 			leftSum = sm
# 	sm = 0
# 	for i in range(mid, len(arr)):
# 		sm += arr[i]["value"]
# 		if sm > rightSum:
# 			rightSum = sm
# 	return max(leftSum, rightSum, leftSum+rightSum)

# def divideAndConquer(arr):
# 	if len(arr) == 1:
# 		return arr[0]["value"]
	
# 	mid = len(arr) // 2
# 	leftArr = arr[0:mid]
# 	rightArr = arr[mid:]

# 	ls = divideAndConquer(leftArr)
# 	rs = divideAndConquer(rightArr)
# 	return max(ls, rs, crossSum(arr))

# regions = [
# 	{
# 		"id" : "A",
# 		"value" : 3
# 	},
# 	{
# 		"id" : "B",
# 		"value" : -5
# 	},
# 	{
# 		"id" : "C",
# 		"value" : 2
# 	},
# 	{
# 		"id" : "D",
# 		"value" : 11
# 	},
# 	{
# 		"id" : "E",
# 		"value" : -8
# 	},
# 	{
# 		"id" : "F",
# 		"value" : 9
# 	},
# 	{
# 		"id" : "G",
# 		"value" : -5
# 	}
# ]

# print(divideAndConquer(regions))



