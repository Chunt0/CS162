from time import time

def c_to_f(c):
    return c*9/5+32

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

t0 = time()
factorial(900)
t1 = time()

print("t1 - t0 = ", t1 - t0)
