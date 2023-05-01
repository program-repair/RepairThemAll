def top_k(lst, k):
	top_lst = []
	for i in range(0, k):
		top_lst += [max(lst)]
		lst.remove(max(lst))
	return top_lst
