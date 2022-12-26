import itertools
import math
print('############### Matrix/Loops #################')
m = n = 9
for i in range(m*n):print(i//n, i%n)

print('############### Variables ####################')
X,Y,Z,A,B=-10,4,5,5,6 # Bet there's even fast ways... 

print('############### Conditionals #################')
print([B,A][X==Y]) # this evaluates to false (which is 0) so B is printed, since it's the zeroith item in the list
print([B,A][0<X<10]) # if X is between 0 and 10, print A, else B (A is the zeroith item in the list, B is the first)
print([A,B][X>0and Z>0and Y<X]) #31 Chars
print([A,B][Z>0<X>Y]) #21 Chars
#Note that you can leave the space out before
#an operator if it is preceded by a number!

print('################## Output ####################')
C = 'yes' == 'no' 
print([5,50][C]) # these have the same
print(5+45*C)    # outputs (you just add the difference to the second number)

C = 'yes' == 'yes' 
print([5,50,60][C]) # these have the same
print(5+45*C)    # outputs (you just add the difference to the second number)

# But we can go deeper, if the second number is only 1 more than the first
print([6,7][C]) # becomes...
print(6+C) # since adding false (0) to 6 is still 6, and adding 1, is 7

# Then there's if one of the two numbers is 1
print([1,567][C])
print(567**C) # since number ** 0 is always 1, and 1 ** number is always number

# This can get stupid with python
print(C*'what'or'hmm') # hard to understand what python is actually doing here, 
                       # but if c is 1, it produces 'what'

D = 1
print(['what', 'four', 'how'][D]) #31 chars
print('wfhhooauwtr'[D::3]) #26 chars (every 3rd character with an offset)

# You can use print's formatting tools to save characters for any iterable
print(', '.join(['A','B'])) # 27 Chars
print(['A','B'],sep=', ') # 26 Chars

print('################ For Loops ###################')
for a in range(3):
  for b in range(5):
    print(a,b)
# Basics: Nesting only required 1 space
# Simplified by removing uneeded indents.
for a in range(3):
 for b in range(5):print(a,b)

# Python modulo % to the rescue
X,Y=2,5
print("classic/nested:")
for a in range(X):
 for b in range(Y):print(a,b) #48 Chars


X,Y=5,2 # reversed
print("modulo:")
for a in range(X*Y):print(a//X,a%X) #35 Chars
# // just divides and only returns the whole number
# So it takes a whole "cycle" of X, before a//X returns 1, and another 5 to produce 2 and so on
# Then modulo returns the remainder in a similar fashion
# 0%5 is still 0, but 1%5
# (modulo just returns the remainder of division... so 1 goes in to 5 0th times + 1 remainder)

def foo():print('hi')

# Cases where the value of the control variable is irrelevant, we can drop range() entirely:
for a in range(10):foo() #24 Chars
for a in[1]*10:foo() #20 Chars, we've just created a list of 1s with 10 items

print('No for:')
# …or get rid of the for loop as a whole:
exec("foo();"*10) #17 chars

# other craziness
for a in range(5):print('other craziness')
for a in '01234':print('other craziness') # 1 shorter

# other craziness 2 (when you need the control variable too)
for a in range(4):print('other craziness 2')
for a in 0,1,2,3:print('other craziness 2') # 1 shorter

print('############# Variable Conversion ############')
A,B=150,11
x=math.floor(A/B) #17 Chars
print(x)
x=math.ceil(A/B) #16 Chars
print(x)

# Both operations can be made a lot shorter:
x=A//B #6 Chars (floor)
print(x)
x=-(-A//B) #10 Chars (ceil)
print(x)

# Converting an iterable to a list
A=list(range(10))
B=list('abc')

# Starred assignment can make the whole thing shorter
*A,=range(10)
*B,='abc'

# Unpacking is similar
A,B,C='a','b','c'
A,B,C='abc'

print(A)
for v in A,B,C:print(v)

# Save chars by assigning common functions names to variables
# a,b,c=input(),input(),input()
# i=input;a,b,c=i(),i(),i() # saved 5 chars!

print('############# Lists ##########################')
L=['a','b','c']
A,B=4,[] #8 Chars
A,*B=4, #7 Chars

#Getting first item
A=L[0] #6 Chars
A,*_=L #6 Chars

#Getting last item
A=L[-1] #7 Chars
*_,A=L #6 Chars

#Removing first item
L.pop(0) #8 Chars
L=L[1:] #7 Chars
_,*L=L #6 Chars

#Removing last item
L=L[:-1] #8 Chars
L=['a','b','c']
L.pop() #7 Chars
L=['a','b','c']
*L,_=L #6 Chars
print(L)

A='d'
B=['e','f', 'g']
L=['a','b','c']

L.append(A) #11 Chars #Appending an item
L+=[A] #6 Chars

L.extend(B) #11 Chars #Extending a list (extend adds iterable values rather than the whole lot)
L+=B #4 Chars

L.insert(i,A) #13 Chars #Inserting items into a list
L[:i]+=A #8 Chars

print(L)
 
# L=L.reverse() #13 Chars #Reversing a list
L=L[::-1] #9 Chars

print(L)

# Retrieving items from back of list a more elegant way
A=0
L[::-1][A] #10 Chars
L[~A] #5 Chars
print(L[::-1][A])
print(L[~A])


print('############# Combinations ###################')
A=itertools.combinations("0123456789", 4)
# print(len(A)) # TypeError!
print(len(list(A))) # 19 Chars
A=itertools.combinations("0123456789",4)
print(len([*A])) # 16 Chars