def sort(lst):
	newlst=[]
	while lst:
		
		minimum=lst[0]
		for x in lst:
			if x>minimum:
				minimum=x
		newlst.append(minimum)
		lst.remove(minimum)
	return newlst
	
def top_k(lst, k):
    lst=sort(lst)
    return lst[:k]
    # Fill in your code here

