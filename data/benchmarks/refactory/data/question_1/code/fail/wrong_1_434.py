def search2(x,seq):
    for i,elem in enumerate(seq):
        counter = 0
        if x<= elem:
            counter = i
        else:
            counter = len(seq)
    return counter
        
