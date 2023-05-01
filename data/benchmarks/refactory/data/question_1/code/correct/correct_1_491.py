def search(x, seq):
	position = 0
	for element in seq:
		if x <= element:
			return position
		else:
			position += 1
	return position
