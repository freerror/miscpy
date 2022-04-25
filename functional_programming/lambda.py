# Syntax: lambda [arguments] : [expression]
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
from typing import Callable

x: Callable[[int | float], int | float]

x = lambda a: a + 10
print(x(20))

# type hint
x2: Callable[[int | float, int | float], int | float]

x2 = lambda a, b: a * b
print(x2(20, 600))

# Their power is shown a bit better below
def myfunc(n: int | float) -> Callable[[int | float], int | float]:
    return lambda a: a * n


mytwentyfiver = myfunc(25)  # mytwentyfiver is a dynamically created lambda

print(mytwentyfiver(11))

# Business usecase: Use lambda functions when an anonymous function is required for a short period of time.

# Other usecase: Code golf, but often list comprehensions and generators are better
