def quick_sort(arr):
	if len(arr) < 2:
		return arr
	else:
		pivot = arr[0]
		less = [i for i in arr[1:] if i <= pivot]
		great = [i for i in arr[1:] if i > pivot]
		return quick_sort(less) + [pivot] + quick_sort(great)

value = [10, 2, 80 , 1, 34]

print(quick_sort(value))