def order (lst):
	for i in range(len(lst)):
		for j in range(i+1, len(lst)):
			if lst[j] < lst[i]:
				lst[i], lst[j] = lst[j], lst[i]
	return lst
	
def top_k(lst, k):
	result = []
	a = order(lst)
	counter = 0
	while counter < k:
		result.append(a.pop())
		counter +=1
	return result
