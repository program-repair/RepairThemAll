def top_k(lst,k):
	if len(lst) == 0:
		return lst
	largest = 0
	newlist = []
	for i in range(k): 
		for item in lst:
			if item >= largest:
				largest = item
		lst.remove(largest)
		newlist.append(largest)
		if len(lst) == 0:
			break
		largest = lst[0]
	return newlist
