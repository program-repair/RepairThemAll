def top_k(lst, k):
    sotsot = []
    while len(sotsot) <=k:
        sotsot.append(max(lst))
        lst.remove(max(lst)) #wont return u any value just modified the list only.
    return sotsot 
    
