def search(x,seq):
	position = tuple(enumerate(seq))
	if len(seq) == 0:
		return 0
	else:
		for i in position :
			if x <= i[1]:
				return i[0]
		return len(seq)
