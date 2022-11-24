import random
import math

continue_roulette=True

input_arr=[]

money=int(input('enter total money: '))

while(continue_roulette):

    type=input('type of bet, for bet enter 1, for 12 enter 2, for odd/even enter 3, for high/low, enter 4: ').split()
    
    if '1' in type:
        bet=input('bet on: ') #1-36

    if '2' in type:
        bet=input('first,second,third: ') #1,2,3

    if '3' in type:
        bet=input('odd or even: ') #1,2

    if '4' in type:
        bet=input('first,second: ') #1,2

    betting_amount=int(input('Enter the betting amount: '))

    input_arr.append([betting_amount,type,bet])

    temp=input('one more? Y/N: ')

    if temp=='N' or temp=='n':continue_roulette=False


roll=random.randint(1, 36)

print('roll is ', roll)

rollbet=str(math.ceil(roll/12))

if roll%2==1: rolloddeven=1
else: rolloddeven=2

if roll<19: rolllowhigh=1
else: rolllowhigh=2

roll = str(roll)
rollbet = str(rollbet)
rolloddeven = str(rolloddeven)
rolllowhigh = str(rolllowhigh)

for [betting_amount,type,bet] in input_arr:
    #payout for type 1
    if '1' in type:
        if bet==roll:
            payout = 35*betting_amount
            money+=payout
        else:
            money-=betting_amount
    #payout for type 2
    if '2' in type:
        if bet==rollbet:
            payout = 2*betting_amount
            money+=payout
        else:
            money-=betting_amount
    #payout fo type 3
    if '3' in type:
        if bet==rolloddeven:
            payout = betting_amount
            money+=payout
        else:
            money-=betting_amount
    #payout for type 4
    if '4' in type:
        if bet==rolllowhigh:
            payout = 1*betting_amount
            money+=payout
        else:
            money-=betting_amount

print('Final money is ', money)

#SHEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEESH
