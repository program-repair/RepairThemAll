def sort_age(lst):
	if len(lst) < 2:
		return lst
	mid = len(lst) // 2
	left = sort_age(lst[:mid])
	right = sort_age(lst[mid:])
	return merge(left, right)
	
def merge(left, right):
	a = []
	while left and right:
		if left[0][1] < right[0][1]:
			a.append(right.pop(0))
		else:
			a.append(left.pop(0))
	a.extend(left)
	a.extend(right)
	return a
