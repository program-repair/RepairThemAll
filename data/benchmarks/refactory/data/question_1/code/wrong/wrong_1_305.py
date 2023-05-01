def search(x, seq):
    for i,v in enumerate(seq):
        if x>v and i!=len(seq)-1:
            continue
        elif x>v and i==len(seq)-1:
            return i+1
        else:
            break
        
    return i
