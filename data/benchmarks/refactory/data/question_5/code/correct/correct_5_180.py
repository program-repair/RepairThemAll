def top_k(lst, k):
    def rank(lyst):
        if len(lyst)==1:
            return list(lyst)
        else:
            a = max(lyst)
            lyst.remove(a)
            return [a]+ rank(lyst)
    new_list = rank(lst)
    return new_list[:k]
