def partition(arr, l, r):
	pivot = arr[r]
	i = l
	for j in range(l, r):
		if arr[j] < pivot:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
	arr[i], arr[r] = arr[r], arr[i]
	return i

def meaningful(arr, k):
	index = partition(arr, 0, len(arr)-1)
	if index == k-1:
		return arr[index]
	if index > k-1:
		return meaningful(arr[:index], k)
	return meaningful(arr[index+1:], k-(index+1))

arr = [999,2,5,16,1,343,3,67,32]
k = 4
print(f'arr : {arr}, {k}th meaningful result is : {meaningful(arr, k)}')
