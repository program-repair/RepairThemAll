
def sort_age(lst):
	newlst=[]
	while lst:
		minimum1=lst[0]
		minimum=lst[0][1]
		for x in lst:
			if x[1]>minimum:
				minimum=x[1]
				minimum1=x
		newlst.append(minimum1)
		lst.remove(minimum1)
	return newlst
