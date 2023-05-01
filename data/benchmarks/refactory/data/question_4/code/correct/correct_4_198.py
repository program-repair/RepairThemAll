def sort_age(lst):
	result = []
	while lst:
		largest = lst[0]
		for x in lst:
			if x[1] > largest[1]:
				largest = x
		lst.remove(largest)
		result.append(largest)
	return result
