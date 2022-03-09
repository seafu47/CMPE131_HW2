def sort_list(listA):
	n=len(listA)
	i=0
	while i < n-1:
		j = 0
		while n-1-i > j:
			if listA[j] >  listA[j+1]
				listA[j], listA[j+1] = listA[j+1], listA[j]
			j = j +1
		i = i + 1
	return listA
