def callback_function(input, input2, callback):
    return input, input2, callback()


def do_something():
    return "fucking hell"


for thing in callback_function("hi", "oof", do_something):
    print(thing)
