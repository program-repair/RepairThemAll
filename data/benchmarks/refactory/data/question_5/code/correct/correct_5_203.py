def top_k(lst, k):
    def sort(lst):
        sort_list = []
        while lst: # a is not []
            biggest = lst[0]
            for element in lst:
                if element > biggest:
                    biggest = element
            lst.remove(biggest)
            sort_list.append(biggest)
        return sort_list
    return sort(lst)[:k]
