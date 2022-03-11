def func_counter(func):
  def wrapper():
        wrapper.counter += 1
        return func()
  wrapper.counter = 0

  return wrapper

@func_counter
def foo():
    return 1

foo()
foo()

print(foo.counter)
