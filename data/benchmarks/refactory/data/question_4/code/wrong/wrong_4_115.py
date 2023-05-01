def sort_age(lst):
    # Fill in your code here
    if lst == ():
        return lst
        
    out = [lst[0],]
    for ele in lst[1:]:
        for indx in range(len(out)):
            if out[indx][1] < ele[1]:
                out.insert(indx, ele)
                break
            elif indx == len(out) - 1:
                out.append(ele)
    return out
