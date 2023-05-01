def top_k(lst, k):
    # Fill in your code here
    def sort(lst):
        sorted_list = []
        while lst:
            largest = lst[0]
            for element in lst:
                if largest < element:
                    largest = element
            lst.remove(largest)
            sorted_list.append(largest)
        return sorted_list
    return sort(lst)[:k]
    pass
