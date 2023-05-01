def sort_age(lst):
    result = []
    while lst:
        heights= map(lambda x:x[1],lst)
        tall=max(heights)
        person=list(filter(lambda x:x[1]==tall,lst))
        result += person
        lst.remove(person[0])
    return result
    
    
