"""The strategy pattern is a design pattern that enables selecting
an algorithm at runtime. Instead of implementing a single algorithm
directly, code receives run-time instructions as to which in a family
of algorithms to use.
"""

def strategy_1():
    print("run strategy 1")

def strategy_2():
    print("run strategy 2")

def strategy_3():
    print("run strategy 2")

def consumer(run_strategy):
    run_strategy()

if __name__ == "__main__":

    deciding_var = 2

    if deciding_var == 1:
        run_strategy = strategy_1
    elif deciding_var == 2:
        run_strategy = strategy_2
    elif deciding_var == 3:
        run_strategy = strategy_3

    consumer(run_strategy)