# 4 years ago
# A was 3 times older than B
# A is 8 years older than B

# Bs age is As age x 3 (4 years ago)

# A-8=B
# (A-4)*3=(B-4)

# Winning solution:

n,m,y=map(int,input().split()) # map run the int function over each of the inputs to convert to ints
a=n//~-m # some kind of crazy hoodoo maths bullshit
print(a+n+y,a+y) # some crazy adding hoodoo