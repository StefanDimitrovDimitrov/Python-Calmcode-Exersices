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
        return number ** n

    return func


pow2 = power(2)
pow3 = power(3)

print(pow2(3))
print(pow3(3))

####################################################
import random


def stopwatch(f):
    def func(*args, **kwargs):
        tic = time.time()
        result = f(*args, **kwargs)
        print(f"this function took: {time.time() - tic}")
        return result

    return func


def sleep_random():
    time.sleep(random.random())
    return "Done!"


timed_sleep = stopwatch(sleep_random)

print(timed_sleep())


###################################################
from functools import wraps

def stopwatch(f):
    @wraps(f)
    def func(*args, **kwargs):
        tic = time.time()
        result = f(*args, **kwargs)
        print(f"this function took: {time.time() - tic}")
        return result

    return func


@stopwatch
def sleep_random():
    '''This string will be propagated by the wraps decorator.'''
    time.sleep(random.random())
    return "Done!"

###############################

def print_call1(f):
    @wraps(f)
    def func(*args, **kwargs):
        tic = time.time()
        result = f(*args, **kwargs)
        print(f"print 1: {time.time() - tic}")
        return result

    return func

def print_call2(f):
    @wraps(f)
    def func(*args, **kwargs):
        tic = time.time()
        result = f(*args, **kwargs)
        print(f"print 2: {time.time() - tic}")
        return result

    return func

@print_call2
@print_call1
def sleep_random():
    '''This string will be propagated by the wraps decorator.'''
    time.sleep(random.random())
    return "Done!"

# we ca have more then one decorator in a stack


######################################################

from retry import retry

import logging

logging.basicConfig()

@retry(ValueError, tries = 5, delay= 0.5)
def randomly_fails(p=0.5):
    if random.random() < p:
        raise ValueError("no bueno!")
    return "Done!"

randomly_fails