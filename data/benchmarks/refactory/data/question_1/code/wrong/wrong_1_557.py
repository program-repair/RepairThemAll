def search(x, seq):
    for i,elem in enumerate(seq):
	    if elem<x:
		    pos=i+1
	    elif elem>x:
		    pos=i
    return pos
