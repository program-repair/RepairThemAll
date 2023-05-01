def top_k(lst, k):
	def sort_num(lst):
		for k in range(len(lst)-1):
			for i in range(k+1, len(lst)):
				if lst[k] < lst[i]:
					lst[k], lst[i] = lst[i], lst[k]
				else:
					continue
		return lst
	slst = sort_num(lst)
	return slst[:k]
