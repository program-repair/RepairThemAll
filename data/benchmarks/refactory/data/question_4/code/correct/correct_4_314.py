def sort_age(lst):
    # Fill in your code here
    sorted_list = []
    while lst:
        tpl = lst[0]
        gender = lst[0][0]
        oldest = lst[0][1]
        for i in lst:
            if i[1] > oldest:
                oldest = i[1]
                tpl = i
                gender = i[0]
        lst.remove(tpl)
        sorted_list.append((gender, oldest))
    return sorted_list
        
