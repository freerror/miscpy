"""In this puzzle you have to write a function taking a list of ints and target
value and return the first pair of ints adding up to the target."""


def get_pair(numbers: list[int], target: int) -> tuple[int, int] | None:
    cache: set[int] = set()
    for n in numbers:
        v = target - n
        if v in cache:
            return v, n
        cache.add(n)


def main():
    print(get_pair([1, 2, 4, 3], 7))


if __name__ == "__main__":
    main()
