def mergeSort(arr):
	if len(arr) == 1:
		return (arr, 0)
	
	lArr, rArr = arr[:len(arr)//2], arr[len(arr)//2:]
	(lArr, rop1), (rArr, rop2) = mergeSort(lArr), mergeSort(rArr)
	rop = rop1+rop2
	
	merged = []
	i, j = 0,0

	while i < len(lArr) and j < len(rArr):
		if lArr[i] <= rArr[j]:
			merged.append(lArr[i])
			i += 1
		else:
			merged.append(rArr[j])
			j += 1
			rop += len(lArr) - i
	while i < len(lArr):
		merged.append(lArr[i])
		i += 1
	while j < len(rArr):
		merged.append(rArr[j])
		j += 1

	return (merged, rop)

arr = [6,7,1,2,3,8]
(arr, total) = mergeSort(arr)
print(f'Number of reversed ordered pairs is : {total}')
