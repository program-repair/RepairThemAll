def sort_age(lst):
	new_lst = []
	while lst:
		biggest = lst[0]
		for i in lst:
			if i[1] > biggest[1]:
				biggest = i
		lst.remove(biggest)
		new_lst.append(biggest)
	return new_lst
