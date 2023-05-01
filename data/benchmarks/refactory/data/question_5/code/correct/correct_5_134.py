def top_k(lst, k):
	lst=sort(lst)
	lst=lst[:k]
	return lst

def sort(lst):
	for i in range(0,len(lst)-1):
		   for j in range(i+1,len(lst)):
			   if lst[i]<lst[j]:
				   lst[i],lst[j]=lst[j],lst[i]
	return lst
