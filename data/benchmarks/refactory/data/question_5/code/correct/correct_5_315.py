def top_k(lst, k):
	def sortedd(lst):
		for j in range(len(lst)-1):
			for i in range(len(lst)-1):
				if lst[i] < lst[i+1]:
					lst[i], lst[i+1] = lst[i+1], lst[i]
		return lst
	return sortedd(lst)[:k]
