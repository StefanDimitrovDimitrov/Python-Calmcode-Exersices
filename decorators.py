import time
import random


def sleep_random():
    time.sleep(random.random())
    return "Done!"


print(sleep_random())


####################################
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def apply(func, a, b):
    return func(a, b)


print(apply(add, 1, 2))
print(apply(sub, 1, 2))


###############################################

def power(n):
    def func(number):
        return number**n
    return func

pow2 = power(2)
pow3 = power(3)

print(pow2(3))
print(pow3(3))
