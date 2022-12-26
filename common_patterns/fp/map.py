# map() executes a specified function for each item in an iterable
# syntax: map(functionname, <iterable>)
def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry')) 

a,b,c,d,e = map(int,input('Enter 5 digits separated by spaces').split())
print(a/2,b*2,c+d,d+a,e-b)