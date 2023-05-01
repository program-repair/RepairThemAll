def remove_extras(lst):
    if lst != []:
    
        my_list = []

        
        for i in range(len(lst)):
            if lst[i] not in my_list:
                my_list.append(lst[i])
        return my_list
    else:
        return []
