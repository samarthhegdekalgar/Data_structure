def find_min(arr):
	small = arr[0]
	index = 0
	for x in range(len(arr)):
		if arr[x] < small:
			small = arr[x]
			index = x
	return index

def selection_sort(arr):
	new_arr = []
	for value in range(len(arr)):
		small = find_min(arr)
		new_arr.append(arr.pop(small))
	return new_arr

arr = [11, 0, 2, 37, 8, 4, 5 , 3]

print(selection_sort(arr))