def doubler(func):
	def wrapper():
		func()
		func()
	return wrapper

@doubler
def hello_word():
	print("hello_word")

hello_word()

