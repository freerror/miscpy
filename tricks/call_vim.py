import sys, tempfile, os
from subprocess import call

EDITOR = os.environ.get('EDITOR','nvim') #that easy!

initial_message = b"" # if you want to set up the file somehow

with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
    tf.write(initial_message)
    tf.flush()
    call([EDITOR, tf.name])

    # do the parsing with `tf` using regular File operations.
    # for instance:
    tf.seek(0)
    edited_message = tf.read()
    print(edited_message.decode("utf-8"))