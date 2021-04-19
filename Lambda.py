def double(x):
    return x * 2

def add_one(x):
    return x + 1

def add_two(x):
    return x + 2

def triple(x):
    return x * 3

number = 1
for func in [add_one, double, add_one]:
    number = func(number)
    print(number)


###############################

number_1 = 1
for func in [lambda x: x+1,lambda x: x * 2, lambda x: x+2]:
    number_1 = func(number_1)
    print(number_1)

####################################

from functools import reduce
numbers = [1, 2, 3, 4, 5]

print(reduce(lambda x, y: x + y, numbers))

####################################
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.normal(0, 1, (11, 2)))
df.columns = ['column_a', 'column_b']
print(df.loc[lambda d: d['column_b'] > 0])

### df.loc - WHAT ?
### [lambda d: d['column_b'] > 0]  - HOW ?