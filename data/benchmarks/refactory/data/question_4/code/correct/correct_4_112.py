def sort_age(lst):
	new = []
	while lst:
		small = lst[0]
		for a in lst:
			if a > small and a[1] > small[1]:
				small = a
		new.append(small)
		lst.remove(small)
	return new
