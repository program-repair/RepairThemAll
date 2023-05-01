def sort(lst):
	a = 0
	for i in range(len(lst)-1):
		if lst[i]<lst[i+1]:
			lst.insert(i,lst[i+1])
			lst.pop(i+2)
			a += 1
	if a == 0:
		return lst
	else:
		return sort(lst)
		
def top_k(lst, k):
    newlist = sort(lst)
    finish = []
    for i in range(k):
        finish.append(lst[i])
    return finish
