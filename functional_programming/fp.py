# sorted vs sort
# avoiding mutability
from functools import partial


z = ["foo", "bar", "420", "69"]
# mutated with sort
z.sort()
print(z)  # ['420', '69', 'bar', 'foo']
# immutable version, using sorted, prefer immutable
z = ["foo", "bar", "420", "69", "REEEEE"]
y = sorted(z)
print(y)  # ['420', '69', 'REEEEE', 'bar', 'foo']

# fanciness using lambda as argument
y2 = sorted(z, key=lambda x: x.lower())
print(y2)  # ['420', '69', 'bar', 'foo', 'REEEEE']


def foo(y: int | float):
    def bar(x: int | float):
        return x + y

    return bar


a = foo(10)
b = a(11)
print(b)

# Iterators
# No examples here, just use these concepts (iterators)
# use itertools funcs like islice()

# Laziness

# Other examples of mutability to avoid
def bar(x: list[int] = [1, 2, 3]):
    x.pop()
    print(x)


bar()  # the default is literally being mutated
bar()  # better to use immutable types for default params (e.g. int, string)

# Functools, cache() and .lru_cache(), cache evaluated functions which have the
# same value to speed up the program.
# Functools partial functions - use them (cautiously)
def do_something(x: int, s: str = "Something"):
    print(f"{x} and {s}")


# wow, whole new functions from partially applied other functions
a = partial(do_something, 15)
a()
a("other thing")
