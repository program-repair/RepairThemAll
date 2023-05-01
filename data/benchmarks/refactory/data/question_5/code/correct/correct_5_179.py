import heapq
def top_k(lst, k):
    k_sorted = heapq.nlargest(k, lst)
    return k_sorted
