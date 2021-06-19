# Syntax: newlist = [_expression_ for _item_ in _iterable_ if _condition_ == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x] # list_item for each list_item in list if 'a' is in list_item
print(newlist)

# Works for any iterables and doesn't have to have conditional
newlist2 = [x/2*3 for x in range(10)]
print(newlist2)

# The expression can be whatever you want including conditions that manipulate the outcome
newlist3 = [x if x != "banana" else "orange" for x in fruits]
print(newlist3)

# The expression can be whatever you want including conditions that manipulate the outcome
newlist4 = ['poopies'[len(x):] if x != "banana" else x[::-1] for x in fruits]
print(newlist4)