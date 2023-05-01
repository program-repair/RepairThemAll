def search(x, seq):
	counter = 0
	for i in seq:
		if x <= i:
			return len(seq[:counter])
		counter = counter + 1
	else:
		return len(seq)
