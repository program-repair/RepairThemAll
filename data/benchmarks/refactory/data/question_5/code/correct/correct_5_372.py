def top_k(lst, k):
    def sort_largest(lst):
        result = []
        while lst and k:
            largest = lst[0]
            index = 0
            for i in range(len(lst)):
                if lst[i] > largest:
                    index = i
                    largest = lst[i]
            result.append(largest)
            lst.remove(largest)
            if len(result) == k:
                break
        return result
    return sort_largest(lst)

