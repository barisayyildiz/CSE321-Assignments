def mergeSort(arr):
	if len(arr) == 1:
		return arr
	
	lArr, rArr = arr[:len(arr)//2], arr[len(arr)//2:]
	lArr, rArr = mergeSort(lArr), mergeSort(rArr)
	
	merged = []
	i, j = 0,0

	while i < len(lArr) and j < len(rArr):
		if lArr[i] <= rArr[j]:
			merged.append(lArr[i])
			i += 1
		else:
			merged.append(rArr[j])
			j += 1
	while i < len(lArr):
		merged.append(lArr[i])
		i += 1
	while j < len(rArr):
		merged.append(rArr[j])
		j += 1

	return merged

arr = [999,2,5,16,1,343,3,67,32]
arr = mergeSort(arr)
print(f'Success Rates : {arr}, The Worst : {arr[0]}, The Best : {arr[-1]}')
