def remove_extras(lst):
	a = []
	for i in lst:
		a = a+[i,]
		if a.count(i)>1:
			a.pop()
	return a
