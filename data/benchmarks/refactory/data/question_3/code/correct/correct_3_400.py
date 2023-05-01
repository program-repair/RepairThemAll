def remove_extras(lst):
	product = []
	for i in lst:
		if i not in product:
			product = product + [i]
	return product
    
    
