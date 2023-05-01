def top_k(lst, k):
	def merge_sort(lst):
		if len(lst) == 0 or len(lst) ==1:
		    	return lst
		mid = len(lst) // 2
		left = merge_sort(lst[:mid])
		right = merge_sort(lst[mid:])
		return merge(left, right)
	def merge(left, right):
		a = []
		while left and right:
			if right[0]<left[0] :
				a.append(left.pop(0))
			else:
				a.append(right.pop(0))
		a.extend(left)
		a.extend(right)
		return a
	return merge_sort(lst)[:k]
