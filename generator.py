# A Python generator is a function that produces a sequence of results, a powerful iterator. 
# Syntax: yield _expression_list_

def numGenny(n):
    number = 0
    for i in range(n):
        yield [number, number/3]
        number += 1
        
for n in numGenny(100):print(n)

# Want a list from that?
nums_and_3rds = list(numGenny(10))

print(nums_and_3rds)

# How they work sort of: Yield differs from return by maintaining its state between calls

# Return is ONLY used to break
def numberGenerator(n):
  if n < 20:
     number = 0
     while number < n:
         yield number
         number += 1
  else:
     return # the return value does nothing so don't even try to return a value

print(list(numberGenerator(15)))

#--------------------->>
# Generator Expression
#--------------------->>

g = (x for x in range(10))
print(list(g))

# Hey! This is similar to list comprehensions like this except the list comprehension is shorter
g = [x for x in range(10)]
print(g) # except the list comprehension is shorter, woohoo GOLF

# They're handy for reduction functions
g = (x for x in range(10))
print(sum(g))
print(g) # print generator object

# the list comprehension version
g = [x for x in range(10)]
print(sum(g))
print(g) # prints list

#--------------------->>
# The send() method!
#--------------------->>
# The below function uses yield expressions, on the right side of an assignment statement
# It's value will be None until the program called the send(value) method
def numberGenerator(n):
     number = yield
     while number < n:
         number = yield number 
         number += 1

g = numberGenerator(11)    # Create our generator
print(next(g)) # note, it's None
# print(next(g)) # this fails because you can't use the < comparitor on None
print(g.send(3))
print(g.send(6))

# Here's a nother example of send()
def double_number(number):
    while True:
        number *= 2
        number = yield number

c = double_number(4)

c.send(None)
print(c.send(5))
print(c.send(3))


#--------------------->>
# Conecting Generators
#--------------------->>
# Syntax: yield from [expression]
print('# Conecting Generators:')
def myGenerator1(val_list):
    for i in val_list:
        yield i

def myGenerator2(m):
    for j in range(1,m+1):
        yield j

def myGenerator3(n, m):
    yield from myGenerator1(n)
    yield from myGenerator2(m)
    # yield from myGenerator2(m, m+5)


print(list(myGenerator3('abcdefghijklmnopqrstuvxyz', 10)))

