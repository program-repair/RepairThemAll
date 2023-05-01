def search(x,seq):
	counter=0
	y=len(seq)
	while counter<y:
		if x>seq[counter]:
			counter+=1
			continue
		break
	return counter
