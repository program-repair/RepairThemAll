def top_k(lst, k):
	counter = 0
	result = []
	while counter < k:
		result.append(max(lst))
		lst.remove(max(lst))
		counter = counter + 1
	return result
