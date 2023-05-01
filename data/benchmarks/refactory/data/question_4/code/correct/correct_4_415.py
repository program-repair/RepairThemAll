
def sort_age(lst):
	a = 0
	for i in range(len(lst) - 1):
		if lst[i][1] < lst[i+1][1]:
			lst.insert(i, lst[i+1])
			lst.pop(i + 2)
			a += 1
	if a == 0:
		return lst
	else:
		return sort_age(lst)
