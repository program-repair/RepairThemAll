def sort_age(lst):
	i = 0
	while i < len(lst)-1:
	    if lst[i][1] > lst[i+1][1]:
	        i += 1
	    elif lst[i][1] < lst[i+1][1]:
	        lst.append(lst[i])
	        lst.remove(lst[i])
	        sort_age(lst)
	return lst
