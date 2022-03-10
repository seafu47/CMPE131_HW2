
def test():
	text = open("document.txt", "r")
	d = dict()
	for line in text:
		line = line.strip()			#convert everything to lowercase
		words = line.split(" ")		#put a space inbetween words

	for word in words:
		if word in d:				#check if word contain in dictionary
			d[word] = d[word] + 1		#increment word count
		else:
			d[word] = 1			#word count stay the same

	#sortx = sorted( x, key = x.get, reverse= True) [:5] 	# sort the list in descending order
	#for i in range(len(sortx)):        			#loop through the 5 unique number
		#print(sortx[i], ":" , x[sortx[i]]) 		# print the word and repeated time

	
	sortbyvalue = {k:v for k, v in sorted(d.items(), key=lambda v: v[1], reverse=True)[:5]}
	newd = dict(sortbyvalue)
	sortbykey = {k:v for k, v in sorted(newd.items())}
	newd1 = dict(sortbykey)
	newd2 ={k:v for k, v in sorted(newd1.items(), key=lambda v: v[1], reverse=True)}
	newd3 = dict(newd2)
	print('\r')
	for key in list(newd3.keys()):
		print(f'{key}: {newd3[key]}')


	











test()
