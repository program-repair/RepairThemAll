def top_k(lst,k):
	def sort_numbers(lst):
		result=[]
		def lame(lst):
			if lst==[]:
				return result
			result.append(max(lst))
			lst.remove(max(lst))
			return lame(lst)
		return lame(lst)
	return sort_numbers(lst)[:k]
