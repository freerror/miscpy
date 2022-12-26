"""The 'water pouring' problem (a.k.a 'two water jug' problem, or the even
cooler 'Die Hard with a vengeance' puzzle) is a puzzle involving a finite
number of water jugs with integer capacities (in this case, measured in
litres). For this problem, we are using only two jugs. Initially, each jug is
empty. We want to find a series of 'steps' to reach a state where one of the
two jugs contain the desired quantity of water

    Inputs:

        Volume of the first jug, a
        Volume of the second jug, b (a<=b)
        The desired quantity of water, n

        Range of possible inputs 0<a,b,n<=100000

    Outputs:

        A list of tuples, with the state of the two jugs after every step
        starting from the first step . This need not be the 'path' with the
        minimum number of steps, but it will surely help for some random
        performance tests

    Valid 'Steps':

        Emptying one jug and doing nothing with the other
        Filling one jug and doing nothing with the other
        Emptying one jug into the other
        Using one jug to fill the other (refer to steps 2 and 6 in the example)

    In short, a valid step consists of pouring water from a source container
    (either of the two jugs or from the infinite source of water) to a
    destination (either of the two jugs or poured outside) until either the
    source container is empty or the destination container is full.
    Example:

    If a=3, b=5, n=4, the steps could be:

    Start from (0,0)

        Fill the second jug (0,5) (Note that the first step is the first step with either of the jugs filled)
        Empty 3 litres from second jug to first jug (3,2)
        Empty first jug (0,2)
        Empty 2 litres from second jug to first jug (2,0)
        Fill second jug (2,5)
        Empty 1 litre from second jug to first jug (3,4). We've reached a state
        where one of the jugs contains the desired quantity of water n=4.

    (The next step of emptying the first jug is redundant, but having the last
    step as (0,4) does not amount to a wrong answer)

    (0,0)->(0,5)->(3,2)->(0,2)->(2,0)->(2,5)->(3,4)

    The function can return

    [(0,5), (3,2), (0,2), (2,0), (2,5), (3,4)]

    Note:

        Assume that you have an infinite supply of water to use.
        Both jugs start out empty, you can choose to fill either of them.
        If the goal cannot be reached in one jug alone return an empty list [].
        All inputs will be > 0
        Learn more about this puzzle

"""

from collections import deque
import functools


@functools.cache
def wpp(max_a: int, max_b: int, goal: int):
    if goal > max_a and goal > max_b:
        return []
    start = ((0, 0),)
    seen: set[tuple[tuple[int, int], ...]] = {start}
    queue: deque[tuple[tuple[int, int], ...]] = deque([start])
    best_seen: list[tuple[int, int]] = []

    while queue:

        steps = queue.popleft()
        ca, cb = steps[-1]

        seen.add(steps)

        steps_list = list(steps)

        if ca == goal or cb == goal:
            candidate = list(steps[1:])
            return candidate
            # if len(best_seen) == 0 or len(candidate) < len(best_seen):
            #     best_seen = candidate

        for na, nb in (
            (ca, max_b),  # ignore a, fill b
            (max_a, cb),  # ignore b, fill a
            (0, cb),  # empty a
            (ca, 0),  # empty b
            (0, cb + ca),  # empty a to b
            (ca + cb, 0),  # empty b to a
            (ca - (r := max_b - cb), cb + r),  # fill b from a
            (ca + (r := max_a - ca), cb - r),  # fill a from b
        ):
            # check validity of action
            if not (0 <= na <= max_a and 0 <= nb <= max_b):
                continue
            new_steps = steps_list[:]
            new_steps.append((na, nb))
            new_steps = tuple(new_steps)
            if new_steps in seen or (na, nb) in steps:
                continue
            queue.append(new_steps)
    return best_seen


def main():
    # steps = wpp(395, 1205125, 3)
    # steps = wpp(3, 5, 4)
    steps = wpp(7, 15, 6)
    # steps = wpp(6, 10, 7)
    print(steps)


if __name__ == "__main__":
    main()
