def remove_extras(lst):
	newlst = []
	for i in lst:
		if i not in newlst:
			newlst.append(i)
	return newlst
    
