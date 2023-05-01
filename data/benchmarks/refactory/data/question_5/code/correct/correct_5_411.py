def top_k(lst, k):
    a = mysort(lst)
    return a[:k]
    pass
def mysort(lst):
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
