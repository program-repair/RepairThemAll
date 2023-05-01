def sort_age(lst):
	newlst = []
	while lst:
		oldest = lst[0]
		for element in lst:
			if element[1] > oldest[1]:
				oldest = element
		lst.remove(oldest)
		newlst.append(oldest)
	return newlst
