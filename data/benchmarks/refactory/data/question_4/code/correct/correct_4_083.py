def sort_age(lst):
    decoy = []
    decoy2 = []
    final = []
    for i in lst:
        decoy.append(i[1])
    while decoy != []:
        decoy2.append(max(decoy))
        decoy.remove(max(decoy))
    for i in decoy2:
        for j in lst:
            if i == j[1]:
                final.append(j)
    return final
    
    
