def top_k(lst,k):
    def top(lst):
        s = []
        while lst:
            smallest = lst[0]
            for element in lst:
                if element>smallest:
                    smallest = element
            lst.remove(smallest)
            s.append(smallest)

        return s
    s = top(lst)
    return s[:k]
