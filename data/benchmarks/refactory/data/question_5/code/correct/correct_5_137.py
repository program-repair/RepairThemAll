def sort_by_value(lst):
	final=[]
	while lst:
		largest=lst[0]
		for i in lst:
			if largest<i:
				largest=i
		lst.remove(largest)
		final.append(largest)
	return final
	
def top_k(lst,k):
    return sort_by_value(lst)[:k]
