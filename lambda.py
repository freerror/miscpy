# Syntax: lambda [arguments] : [expression]
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
x = lambda a : a + 10
print(x(20))

x = lambda a, b : a * b
print(x(20, 600))

# Their power is shown a bit bettter below
def myfunc(n):
  return lambda a : a * n

mytwentyfiver = myfunc(25) # mytwentyfiver is a dynamically created lambda

print(mytwentyfiver(11))

# Business usecase: Use lambda functions when an anonymous function is required for a short period of time.

# Other usecase: Code golf, but often list comprehensions and generators are better