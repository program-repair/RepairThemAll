def search(x, seq):
	counter = 0
	for i in seq:
		counter += 1
		if x <= i:
			return counter-1
	return len(seq)
