"""The factory method pattern is a pattern that uses
methods to deal with the problem of creating objects
without having to specify the exact class of the object
that will be created. This is done by creating objects
by calling a factory method—either specified in an interface
and implemented by child classes, or implemented in a base
class and optionally overridden by derived classes—rather
than by calling a constructor.
"""

def behaviour_1():
    print("doing behaviour 1")

def behaviour_2():
    print("doing behaviour 2")

def behaviour_3():
    print("doing behaviour 3")

def factory(deciding_condition):
    # do other stuff

    # now do factory pattern stuff
    if deciding_condition == 1:
        return behaviour_1
    elif deciding_condition == 2:
        return behaviour_2
    elif deciding_condition == 3:
        return behaviour_3

if __name__ == "__main__":
    deciding_condition = 3

    # do stuff

    # now factory stuff
    appropriate_behaviour = factory(deciding_condition)

    appropriate_behaviour()