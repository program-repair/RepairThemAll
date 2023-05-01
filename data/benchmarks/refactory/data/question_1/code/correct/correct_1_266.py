def search(x, seq):
    output = 0
    for j in seq:
        if x>j:
            output +=1
    return output

