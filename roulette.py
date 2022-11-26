import random
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import math

#Roulette structure
european_roulette = []
#CUrrently the double zero of US roulette is taken as 37 as it is creating problem with int datatype
american_roulette = [37]
for i in range(37):
    european_roulette.append(i)
    american_roulette.append(i)

#print(american_roulette)
#print(european_roulette)


roll_array = []
def rotate_roulette(roulette, turns=1):
    for i in range(turns):
        roll = random.choice(roulette)
        roll_array.append(roll)
    return roll_array

rotate_roulette(american_roulette, turns=5)



# bet is the class containing all the possible type of betsn inputs are betting_amount(int) and respective betting type (list or array)
roll = roll_array[0]
class bet:

    def __init__(self, betting_amount):
        self.betting_amount = betting_amount
        
    def single_bet(betting_amount, digits):
        payout_money = (betting_amount*35*digits.count(roll)) - (betting_amount*(len(digits)- digits.count(roll)))
        betting_amount += payout_money
        print(betting_amount)

    def odd_even_bet(betting_amount, odd_even_bet):
        if slot%2 == 1:
            roll_oddeven = 1
        elif slot%2 == 0:
            roll_oddeven = 2
        payout_money = (odd_even_bet.count(roll_oddeven) * betting_amount) - ((len(odd_even_bet) - odd_even_bet.count(roll_oddeven)) * betting_amount)
        betting_amount += payout_money

    def twelve_bet(betting_amount, dozen_bet):
        roll_dozen = (math.ceil(roll/12))
        payout_money = (dozen_bet.count(roll_dozen) * 2 * betting_amount) - ((len(dozen_bet) - dozen_bet.count(roll_dozen)) * betting_amount)
        betting_amount += payout_money

    def eighteen_bet(betting_amount, eighteen_bet):
        roll_eighteen = math.ceil(roll/18)
        payout_money = (eighteen_bet.count(roll_eighteen) * betting_amount) - ((len(eighteen_bet) - eighteen_bet.count(roll_dozen)) * betting_amount)

    def column_bet(betting_amount, column_bet):
        pass



#bet1 = bet.single_bet(betting_amount=100, digits=[1,2,3,4,5,6,7,8])
bet2 = bet.twelve_bet(200, [1, 2])
print(betting_amount)
print('This is roll', roll)
print(type(roll))


