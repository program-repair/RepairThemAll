def top_k(lst, k):
	new_lst = []
	cut_lst = []
	while lst:
		biggest = lst[0]
		for i in lst:
			if i > biggest:
				biggest = i
		lst.remove(biggest)
		new_lst.append(biggest)
	for i in range(k):
		cut_lst.append(new_lst[0])
		new_lst.pop(0)
	return cut_lst
