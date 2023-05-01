def top_k(lst, k):
	sorted = []
	while lst:
		largest = lst[0]
		for i in lst:
			if i > largest:
				largest = i
		sorted.append(largest)
		lst.remove(largest)
	return sorted[:k]
