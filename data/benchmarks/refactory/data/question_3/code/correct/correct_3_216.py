def remove_extras(lst):
	final=[]
	for i in lst:
		if i not in final:
			final+=[i,]
		else:
			continue
	return final

