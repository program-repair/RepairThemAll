def top_k(lst, k):
	if lst == [] or k == 0:
		return []
	sort = []
	while lst:
		largest = lst[0]
		for element in lst:
			if element > largest:
				largest = element
		lst.remove(largest)
		sort.append(largest)
		if len(sort) > k-1:
			break
	return sort
