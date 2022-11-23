import random
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

#Roulette structure
european_roulette = []
american_roulette = ["double zero"]
for i in range(37):
    european_roulette.append(i)
    american_roulette.append(i)

#print(american_roulette)
#print(european_roulette)

#All the bet positions
even_bets = []
odd_bets = []

red_bets = []
black_bets = []

first_twelve_bets = []
second_twelve_bets = []
third_twelve_bets =[]

first_eighteen_bets = []
second_eighteen_bets = []

column1_bets = []
column2_bets = []
column3_bets = []

zeroes_bets = []
single_bets = []

slot_array = []
def rotate_roulette(roulette, turns=1):
    for i in range(turns):
        slot = random.choice(roulette)
        slot_array.append(slot)
    print(slot_array)

rotate_roulette(american_roulette, turns=5)

bet_type = [even_bets, odd_bets, red_bets, black_bets, first_twelve_bets, second_twelve_bets, third_twelve_bets, first_eighteen_bets, second_eighteen_bets, column1_bets, column2_bets, column3_bets, zeroes_bets, single_bets]





