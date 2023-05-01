def remove_extras(lst):
	if lst == []:
		return []
	elif lst[-1] in lst[:-1]:
		return remove_extras(lst[:-1])
	else:
		return remove_extras(lst[:-1]) + [lst[-1]]
