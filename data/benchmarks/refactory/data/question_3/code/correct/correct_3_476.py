from collections import OrderedDict

def remove_extras(lst):
    return list(OrderedDict.fromkeys(lst)) 
  
