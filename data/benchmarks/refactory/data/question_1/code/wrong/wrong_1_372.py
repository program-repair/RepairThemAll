def search(x, seq):
    lst1 = list(seq)
    if lst1 == []:
        return 0
    else: 
        length = len(lst1)
        lst2 = []
        if x < seq[0]:
            lst2 = [x] + lst1
        elif x > seq[length -1]:
            lst2 = lst1 + [x]
        else:
            for i in range(0, length):
                if seq[i] <= x <= seq[i+1]:
                    lst2 = lst1[:i+1] + [x] + lst1[i+1:]
    for i in range(len(lst2)):
        if x == lst2[i]:
            return i
