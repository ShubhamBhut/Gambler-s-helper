import random
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

european_roulette = []
american_roulette = ["double zero"]
for i in range(37):
    european_roulette.append(i)
    american_roulette.append(i)

print(american_roulette)
print(european_roulette)

def rotate_roulette(roulette):
    slot = random.choice(roulette)
    print(slot)

rotate_roulette(american_roulette)

