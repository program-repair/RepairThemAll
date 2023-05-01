def search(x, seq):
	position = 0
	for i in seq:
		if x > i:
			position = seq.index(i) + 1
		else:
			position = seq.index(i)
			break
	return position
