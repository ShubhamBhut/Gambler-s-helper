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
        
    def single_bet(self, digits):
        payout_money = (self.betting_amount*35*digits.count(roll)) - (self.betting_amount*(len(digits)- digits.count(roll)))
        self.betting_amount += payout_money
        return self.betting_amount

    def odd_even_bet(self, odd_even_bet):
        if roll%2 == 1:
            roll_oddeven = 1
        elif roll%2 == 0:
            roll_oddeven = 2
        payout_money = (odd_even_bet.count(roll_oddeven) * self.betting_amount) - ((len(odd_even_bet) - odd_even_bet.count(roll_oddeven)) * self.betting_amount)
        self.betting_amount += payout_money
        return self.betting_amount

    def twelve_bet(self, dozen_bet):
        roll_dozen = (math.ceil(roll/12))
        payout_money = (dozen_bet.count(roll_dozen) * 2 * self.betting_amount) - ((len(dozen_bet) - dozen_bet.count(roll_dozen)) * self.betting_amount)
        self.betting_amount += payout_money
        return self.betting_amount

    def eighteen_bet(self, eighteen_bet):
        roll_eighteen = math.ceil(roll/18)
        payout_money = (eighteen_bet.count(roll_eighteen) * self.betting_amount) - ((len(eighteen_bet) - eighteen_bet.count(roll_eighteen)) * self.betting_amount)
        self.betting_amount += payout_money
        return self.betting_amount

    def column_bet(self, column_bet):
        column1 = [1,4,7,10,13,16,19,22,25,28,31,34]
        column2 = [2,5,8,11,14,17,20,23,26,29,32,35]
        column3 = [3,6,9,12,15,18,21,24,27,30,33,36]
        for i in range(12):
            if i in column1:
                roll_column = 1
            elif i in column2:
                roll_column = 2
            elif i in column3:
                roll_column = 3
        payout_money = (column_bet.count(roll_column) * self.betting_amount) - ((len(column_bet) - column_bet.count(roll_column)) * self.betting_amount)
        self.betting_amount += payout_money
        return self.betting_amount






#bet1 = bet.single_bet(betting_amount=100, digits=[1,2,3,4,5,6,7,8])
bet2 = bet(betting_amount=100)
bet3 = bet(69)
print(bet2.odd_even_bet(odd_even_bet=[1]))
print(bet3.eighteen_bet(eighteen_bet=[1]))
print('This is roll', roll)
#print(type(roll))




