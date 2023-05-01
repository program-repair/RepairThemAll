def search(x, seq):
    holder=0
    for value in seq:
        if x>value:
            holder+=1
    return holder
