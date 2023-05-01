def sort_age(lst):
	if len(lst) == 0:
		return lst
	else:
	    smallest = lst[0]
	    newlist = []
	    while lst:
		    for item in lst:
		    	if item[1] <= smallest[1]:
			    	smallest = item
		    lst.remove(smallest)
		    newlist.insert(0,smallest)
		    if len(lst) == 0:
			    break
		    smallest = lst[0]
	    return newlist
	
