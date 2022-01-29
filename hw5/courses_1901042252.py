class Course:
	def __init__(self, name, start, finish):
		self.name = name
		self.start = start
		self.finish = finish
	# used for comparisons
	def __lt__(self, other):
		return self.start < other.start
	# returns string representation
	def __str__(self):
		return f'{self.name} -> [{self.start},{self.finish}]'
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


def maxCourses(courses):
	# result array
	result = []

	# sort the courses by their starting time
	courses = insertionSort(courses)

	# counter, keeps the last course's index
	i = 0
	# add the first course
	result.append(courses[0])
	
	for j in range(1,len(courses)):
		if courses[j].start >= courses[i].finish:
			result.append(courses[j])
			i = j
	return result

courses = [
	Course("English",1,2),
	Course("Mathematics",3,4),
	Course("Physics",0,6),
	Course("Chemistry",5,7),
	Course("Biology",8,9),
	Course("Geography",5,9),
]

print(maxCourses(courses))

