def top_k(lst, k):
    if k == 1:
        return [max(lst)]
    else:
        answer = []
        for i in range(min(k, len(lst))):
            largest = max(lst)
            answer.append(largest)
            lst.remove(largest)
        return answer
