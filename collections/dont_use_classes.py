# So say you don't want to use classes...


def named_tuple_example():
    # You could use typing.NamedTuple
    # Alternative to Classes in Python for holding data

    from typing import NamedTuple, Optional

    # This is the "fallback" syntax used by namedtuple() which typing.NamedTuple is
    # a wrapper for
    Owner = NamedTuple("Owner", [("first_name", str), ("last_name", str)])
    Car = NamedTuple(
        "Car", [("plate_num", str), ("vin", str), ("owner", Owner)]
    )

    car_1 = Car(
        plate_num="DG12321", vin="00053431", owner=Owner("George", "Gerber")
    )

    # access data by name like an object!
    print(car_1.plate_num)
    print(car_1.owner.first_name)

    # arguably superior way to do NamedTuples
    class Truck(NamedTuple):
        """This is a docstring, available when we use the superior class syntax
        (still a NamedTuple, don't worry)"""

        owner: Optional[Owner] = None
        plate_num: str = ""
        vin: str = ""

    # truck has default values (but that's not very useful for an immutable
    # thing
    truck_1 = Truck()

    # Noting that these are IMMUTABLE (which can be expensive for larger
    # objects / collections and frequency of updates)
    # this fails as it's read only
    # truck_1.owner = Owner('Rodger', 'Foo')
    # have to pay the re-instantiate cost:
    truck_1 = Truck(Owner("Rodger", "Foo"), "abc123", "0001232")
    print(truck_1)


def dataclass_example():
    # these are just simple wrapper provided to simplify creating classes that
    # are mostly there to hold data (however, nothing is held back as far as
    # classes are concerned: polymorphism, inheritance, methods, you name it)

    from dataclasses import dataclass

    @dataclass(slots=True)  # <- if you require slots, otherwise no parens
    class Truck:
        plate_num: str = ""
        vin: str = ""

    # mutable
    truck = Truck("123abc", "12324")
    print(truck.plate_num)
    truck.plate_num = "cba321"
    print(truck.plate_num)


def attr_class_example():
    # a slightly more feature_packed alternative library
    # install: `python -m pip install attrs`

    import attr

    @attr.s
    class Truck:
        plate_num: str = attr.ib(converter=str)
        vin: int = attr.ib(validator=attr.validators.instance_of(int))

    truck = Truck(123123, 4442)
    print(truck)
    # raises error:
    # truck_2 = Truck('123abc', '4324')
    # print(truck_2)


def simple_namespace():
    # downside with this is it's less enforced
    # has fairly high getattr time's as well (in simple cases creating a new
    # tuple will be faster)

    from types import SimpleNamespace

    truck = SimpleNamespace(plate_num="123abc", vin=123123)

    class OtherThing(SimpleNamespace):
        name: str
        sign: str = "Libra"

    new = OtherThing("George")
    print(new)

    print(truck.plate_num)
    # also mutable
    truck.plate_num = "cba321"
    print(truck.plate_num)


# Others:
# Pydantic - opinionated, targetted at parsing operations so quite a
# performance hit and have a different purpose compared with other collection types
