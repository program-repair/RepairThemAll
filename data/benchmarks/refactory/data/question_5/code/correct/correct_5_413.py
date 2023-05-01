def top_k(lst,k):
	output = []
	for i in range(k):
		largest = max(lst)
		lst.remove(largest)
		output.append(largest)
	return output
