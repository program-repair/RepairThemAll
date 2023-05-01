def sort(lst):
	sort = []
	while lst:
		largest = lst[0]
		for element in lst:
			if element > largest:
				largest = element
		lst.remove(largest)
		sort.append(largest)
	return sort
	
def top_k(lst, k):
	sorted_list = sort(lst)
	result = sorted_list[:k]
	return result
