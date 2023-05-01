def sort_age(lst):
	newlst = []
	while lst:
		newlst += (max(lst, key = lambda x: x[1]),)
		lst.remove(max(lst, key = lambda x: x[1]))
	return newlst
