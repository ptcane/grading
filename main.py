## Week 2 assignment
# Fix the functions so that they work as expected
# ---------------------------------------------------

def add(a, b):
    return a + b

def subtract(a, b):
    """subtract two numbers: b from a"""
    return a - b

result = 25

import pandas as pd

df = pd.DataFrame({'input': [1,2,3,4,5,6],
                   'output': [2,4,6,8,10,12]
})

out1 = df['output'][2]