def remove_extras(lst):
	new = []
	for element in lst:
		if element not in new:
			new.append(element)
	return new

