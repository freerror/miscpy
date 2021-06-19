# Notes: this is in golf style, not PEP 8 styled 
# multi assign
a,b,c=1,[2, 'two'],'three'
print(a,b,c)

# assign tuple to remaining variable
a,*b=1,2,3,4,5
print(a,b)

# assign same value to multiple variables
a=b=100
a+=1011
b-=99
print(a,b)

# assign multiple variables to mutable types works differently
a=b=[0,1,2,3]

a[0]+=100

print(b) # b changed as It's the same object in memory

v=[1,2,3];c=v;d=v
c[0]+=100
print(c,d) # damn, it still assigned the same value!

# what we really want is to clone the list; slicing technique:
c=[1,2,3];d=c[:] # (this is a "shallow copy" -- wont clone other mutable types in list, e.g. other lists)
c[0]+=100
print(c,d)

# see how this is "shallow"
v=[1,2,3];c=[1,2,v];d=c[:] # (this is a "shallow copy" -- wont clone other mutable types in list, e.g. other lists)
c[0]+=100
v[0]+=100
print(c,d) # it assigned the same value to the nested list

# You can also use the list method to copy lists
c=[1,2,3];d=list(c) # 19 chars, vs 16 above - prev one wins the golf challenge
c[0]+=100
print(c,d)

# is it a shallow copy though?
c=[1,2,[1,2,3]];d=list(c)
c[0]+=100
c[2][0]+=100
print(c,d) # it assigned the same value to the nested list (so yes)

# deepcopy is available...
from copy import deepcopy
c=[1,2,[1,2,3]];d=deepcopy(c)
c[0]+=100
c[2][0]+=100
print(c,d) # c[2][0] and d[2][0] are distinct now

