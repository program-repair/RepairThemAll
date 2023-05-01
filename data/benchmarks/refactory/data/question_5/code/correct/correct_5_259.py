def top_k(lst, k):
	newlst = []
	while len(newlst) < k:
		newlst += (lst.pop(lst.index(max(lst))),)
	return newlst
