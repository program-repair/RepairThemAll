def swap_positions(lst):
	new_lst = []
	for i in range(0, len(lst)):
		new_lst.append((lst[i][1], lst[i][0]))
	return new_lst

def sort_age(lst):
	swapped_lst = swap_positions(lst)
	new_lst =[]
	while (swapped_lst != []):
		new_lst.append(max(swapped_lst))
		swapped_lst.remove(max(swapped_lst))
	return swap_positions(new_lst)
