def sort_age(lst):
	result=[]
	def lame(lst):
		loser=0
		list_of_numbers=[]
		x=len(lst)
		if lst==[]:
			return result
		for i in range(x):
			list_of_numbers+=[lst[i][1]]
		y=max(list_of_numbers)
		for i in lst:
			if i[1]==y:
				loser=i
		result.append(loser)
		lst.remove(loser)
		return lame(lst)
	return lame(lst)
