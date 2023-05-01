def top_k(lst, k):
	for start in range(len(lst)-1):
		maximum = start
		for i in range(start, len(lst)):
			if lst[i] > lst[maximum]:
				maximum = i
		lst[maximum], lst[start] = lst[start], lst[maximum]
	return lst[:k]
