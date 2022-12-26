from dataclasses import dataclass, field
from typing import Any


def list_factory(*args: Any):
    def _list_factory(args: tuple[Any] = args):
        return list(args)

    return _list_factory


@dataclass
class Oops:
    # # not allowed
    # oopsie: list[int] = [10, 10, 10]
    # # not allowed
    # oopsie: list[int] = field(default=[10, 10, 10])
    # # still not allowed
    # oopsie: list[int] = field(default=list([10, 10, 10]))
    # # also error: default factory should be the name of the factory
    # oopsie: list[int] = field(default_factory=list([10, 10, 10]))

    # this closure works
    oopsie: list[int] = field(default_factory=list_factory(10, 10, 10))


def main():
    oops_1 = Oops()
    oops_2 = Oops()
    oops_2.oopsie[0] = 20

    print(oops_1.oopsie[0] is not oops_2.oopsie[0])
    print(oops_1.oopsie)
    print(oops_2.oopsie)


if __name__ == "__main__":
    main()
