def sort_age(lst):
	new_lst = []
	while lst:
		oldest = lst[0][1]
		for people in lst:
			if people[1] >= oldest:
				oldest = people[1]
				remove_people = people
		new_lst.append(remove_people)
		lst.remove(remove_people)
	return new_lst
