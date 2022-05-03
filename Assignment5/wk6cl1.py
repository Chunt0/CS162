# Christopher Hunt
# CS162
# Understanding super() __init__()

def my_gen(x=0):
    while x<100000:
        yield x
        x += 1

gen = my_gen()

for i in gen:
    print(i)

