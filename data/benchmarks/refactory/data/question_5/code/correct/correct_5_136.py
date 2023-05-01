def top_k(lst, k):
	new_lst = lst
	end = []
	for a in range(k):
		end.append(max(new_lst))
		new_lst.remove(max(new_lst))
	return end
