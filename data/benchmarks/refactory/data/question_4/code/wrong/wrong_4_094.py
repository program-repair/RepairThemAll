def sort_age(lst):
	lst.sort(key=lambda tup:tup[1], reverse = True)
	return lst
