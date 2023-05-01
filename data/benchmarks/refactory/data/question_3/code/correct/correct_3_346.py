def remove_extras(lst):
	current = []
	for i in lst:
		if i in current:
			continue
		else:
			current.append(i)
	return current
