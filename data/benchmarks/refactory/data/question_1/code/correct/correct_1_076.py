def search(value, seq):
	for i in range(len(seq)):
		if value <= seq[i]:
			return i
		else:
			continue
	return len(seq)
