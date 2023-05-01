def sort_age(lst):
	def sort(lst):
		counter = 0
		a = list(lst)
		while counter<len(lst):
			previous = a[0]
			for i in range(1,len(lst)):
				if a[i]>previous:
					a[i-1]=a[i]
					a[i]=previous
				else:
					previous = a[i]
			counter += 1
		return a
	A = list(map(lambda x:x[1],lst))
	a = sort(A)
	b = []
	for i in a:
		for y in lst:
			if y[1]==i:
				b.append(y)
	return b
        
