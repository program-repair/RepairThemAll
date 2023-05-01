def search(x, seq):
    counter=0
    for i in seq:
        if i>=x:
            break
        counter=counter+1
    return counter
