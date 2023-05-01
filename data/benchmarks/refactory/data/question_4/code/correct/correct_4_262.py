def sort_age(lst):
	for k in range(len(lst)-1):
		for i in range(k+1, len(lst)):
			if lst[k][1] < lst[i][1]:
				lst[k], lst[i] = lst[i], lst[k]
			else:
			    continue
	return lst
