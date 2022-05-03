# Scoop
Currently I just fixed the function match_word() located in ldrow_funcs.py.
Check out the comments. There's a portion where I was trying to address a particular
error where if you guessed a letter that was in the word but the guess had more
of those characters in it, it would highlight them anyway. This was a no-no. So,
I fixed that but it's a bit of a mess.

Also I need to continue working on the look and feel of the app itself. I would
like to have a list of letters showing their status.

Anyway, feel free to copy this code onto your local machine

Grab everything in this directory, then all you need to do is:
python3 /path/to/wordl/ldrow_driver.py

Have fun!
