def sort_age(lst):
    result = []
    while lst:
        biggest = lst[0]
        for e in lst:
            if e[1] > biggest[1]:
                biggest = e
        result.append(biggest)
        lst.remove(biggest)
    return result

''' read wrong question
def sort_age(lst):
  male = []
  female = []
  for i in range(len(lst)):
    if lst[i][0] == "M":
      male.append(lst[i])
    else:
      female.append(lst[i])
  male.sort()
  female.sort()
  combine = male[::-1] + female[::-1]
  return combine
'''
