def test():
	data = open("document.txt", "r")
	x = dict()
	for line in data:
		#line = data.lower()			#convert everything to lowercase
		words = line.split(" ")		#put a space inbetween words
		
	for word in words:							
		if word in x:				#check if word contain in dictionary
			x[word] = x[word] + 1		#increment word count
		else:
			x[word] = 1			#word count stay the same
		
		#for key in list(x.keys()): 
		 # print ( key, ":" , x[key]) 

	sortx = sorted( x, key = x.get, reverse= True) [:5] 	# sort the list in descending order
	for i in range(len(sortx)-1):        			#loop through the 5 unique number
		print(sortx[i], ":" , x[sortx[i]]) 		# print the word and repeated time

		
	


