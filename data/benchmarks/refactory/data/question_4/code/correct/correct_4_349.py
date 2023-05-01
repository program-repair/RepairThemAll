def sort_age(lst):
	sort=[]
	for ele in lst:
		if sort==[]:
			sort+=[ele]
		else:
			for i in range(len(sort)):
				if ele[1]<sort[i][1] and i==len(sort)-1:
					sort.append(ele)
				elif ele[1]<sort[i][1]:
					continue
				else:
					sort.insert(i,ele)
					break

	return sort

