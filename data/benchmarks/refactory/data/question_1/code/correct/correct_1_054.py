def search(x, seq):
	seq=list(seq)
	if seq==[]:
		return 0
	else:
		for i in seq:
			if x<=i:
				num=seq.index(i)
				break
			else:
				num=len(seq)
	return num
