
def top_k(lst, k):
    # Fill in your code here
    data_list = lst
    new_list = []
    while data_list:
        minimum = data_list[0]  # arbitrary number in list 
        for x in data_list: 
            if x > minimum:
                minimum = x
        new_list.append(minimum)
        data_list.remove(minimum) 
    return new_list[:k]
