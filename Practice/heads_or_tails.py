'''
Challenge 1: create a coin flip game using random module
Practice creating a coin for a con toss.
'''

import random

toss = random.randint(0,1)

if toss == 1:
    print("heads")
else:
    print("tails")
