def top_k(lst, k):
	res=[]
	while len(res)<k:
		res.append(max(lst))
		lst.remove(max(lst))
	return res
