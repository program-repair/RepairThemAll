def top_k(lst,k):
    def selection_sort(lst):
        srt = []
        while lst:
            smallest = lst[0]
            for elem in lst:
                if elem < smallest:
                    smallest = elem
            lst.remove(smallest)
            srt.append(smallest)
        return srt
    return selection_sort(lst)[-1:-k-1:-1]
