def top_k(lst, k):
    result = []
    while lst:
      biggest = lst[0]
      for e in lst:
        if e > biggest:
            biggest = e
      result.append(biggest)
      lst.remove(biggest)
    return result[:k]
