def top_k(lst, k):
    def sort(lst):
        new = [] 
        while lst:
            greatest = lst[0]
            for i in lst:
                if i > greatest:
                    greatest = i 
            lst.remove(greatest)
            new.append(greatest)
        return new
    return sort(lst)[:k]
