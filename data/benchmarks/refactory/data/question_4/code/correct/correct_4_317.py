
    
def sort_age(lst):
    def bubble_sort(lst):
        swap = True
        while swap:
            swap = False
            for i in range(len(lst)-1):
                if lst[i][1]<lst[i+1][1]:
                    lst[i],lst[i+1]=lst[i+1],lst[i]
                    swap =True
        return lst
    return bubble_sort(lst)
