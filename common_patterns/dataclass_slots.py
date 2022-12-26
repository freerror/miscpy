# Slots are more efficient than the underlying __dict__ used by normal classes
# they are available in normal and dataclasses like so:

from dataclasses import dataclass
import time


class PersonSlow:
    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email


class Person:
    __slots__ = "name", "address", "email"

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email


@dataclass(slots=True)
class Person2:
    name: str
    address: str
    email: str


def avg_set_get_del_obj(person: Person | PersonSlow | Person2) -> float:
    times: list[int] = []
    num_tests = 10000000
    for i in range(num_tests):
        start = time.perf_counter_ns()
        person.name = "Judy Smith"
        _ = person.name
        del person.name
        end = time.perf_counter_ns()
        times.append(end - start)
    return sum(times) / num_tests


def main():
    person = PersonSlow(
        "Judy Smith", "23 Diamantis Road", "judy@diamantis.com"
    )
    person1 = Person("Judy Smith", "23 Diamantis Road", "judy@diamantis.com")
    person2 = Person2("Judy Smith", "23 Diamantis Road", "judy@diamantis.com")

    speed_slow = avg_set_get_del_obj(person)
    speed_fast1 = avg_set_get_del_obj(person1)
    speed_fast2 = avg_set_get_del_obj(person2)

    difference_1 = (1 - speed_fast1 / speed_slow) * 100
    difference_2 = (1 - speed_fast2 / speed_slow) * 100

    print(f"PersonSlow avg {speed_slow}ns")
    # around 174ms
    print(f"Person1 avg {speed_fast1}ns, {difference_1:.2f}% improvement")
    # around 14.5% better
    print(f"Person2 avg {speed_fast2}ns, {difference_2:.2f}% improvement")
    # around 19% better


if __name__ == "__main__":
    main()
