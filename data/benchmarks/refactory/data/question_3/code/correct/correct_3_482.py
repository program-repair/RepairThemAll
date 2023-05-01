def remove_extras(lst):
	re=()
	uni=[]
	for ele in lst:
		if ele not in re:
			re+=(ele,)
			uni+=[ele]
		else:
			continue
	return uni
