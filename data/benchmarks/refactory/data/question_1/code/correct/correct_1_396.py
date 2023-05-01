def search(x,seq):
	for i in seq:
		if x <= i:
			return seq.index(i)
	if seq == () or seq == []:
		return 0
	elif x > seq[len(seq)-1]:
		return len(seq)
