import time
def calculate_time(func):
	def wrapper():
		start = time.time()
		func()
		end = time.time()
		x = end - start
		print("Total time" , X)
	return wrapper():

@calculate_time
	def func():
	return (anynumbrr)
	