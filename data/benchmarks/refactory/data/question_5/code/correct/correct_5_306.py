def top_k(lst, k):
	result = []
	while lst:
		biggest = lst[0]
		for item in lst:
			if item > biggest:
				biggest = item
		lst.remove(biggest)
		result.append(biggest)
	return result[:k]
	
