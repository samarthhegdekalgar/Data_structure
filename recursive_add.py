def sum(list1):
	if list1 == []:
		return 0
	return list1[0] + sum(list1[1:])

value = [10, 20, 30, 40]

print(sum(value))