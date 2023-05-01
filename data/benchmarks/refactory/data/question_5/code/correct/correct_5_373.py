def top_k(lst, k):
    new_lst = []
    while lst:
	    high = lst[0]
	    for i in lst:
		    if high < i:
			    high = i
	    new_lst.append(high)
	    lst.remove(high)
    return new_lst[:k]
