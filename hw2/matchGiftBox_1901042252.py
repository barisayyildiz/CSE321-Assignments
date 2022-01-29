def partition(arr, left, right):
	pivot, pIndex = arr[right], right
	right -= 1
	while left <= right:
		while arr[left] < pivot:
			if left == len(arr)-1:
				break
			left += 1
		while right >= 0 and arr[right] > pivot:
			right -= 1
		if left < right:
			arr[left], arr[right] = arr[right], arr[left]
	arr[pIndex], arr[left] = arr[left], arr[pIndex]
	return left		

def quicksort(arr, left, right):
	if left < right:
		idx = partition(arr, left, right)
		quicksort(arr, left, idx-1)
		quicksort(arr, idx+1, right)

# if they are not matching
def testCase(gifts, boxes):
	for i in range(len(gifts)):
		if gifts[i] != boxes[i]:
			return False
	return True

gifts = [6,2,4,9,12,1,7]
boxes = [2,12,7,4,1,6,9]


print(f"Are gifts and boxes matching : {testCase(gifts, boxes)}", end='\n\n')

print(f'Gifts before quick sort : {gifts}')
print(f'Boxes before quick sort : {boxes}', end='\n\n')

quicksort(gifts, 0, len(gifts)-1)
quicksort(boxes, 0, len(boxes)-1)

print(f'Gifts after quick sort : {gifts}')
print(f'Boxes after quick sort : {boxes}', end='\n\n')

print(f"Are gifts and boxes matching : {testCase(gifts, boxes)}")
