import random
import math

money=int(input('Enter the betting amount: '))
type=input('type of bet, for single enter 1, for 12 enter 2, for odd/even enter 3, for high/low, enter 4: ').split()

print(type)
if '1' in type:
    single=input('bet on').split() #1-36

if '2' in type:
    dozen=input('first,second,third').split() #1,2,3

if '3' in type:
    oddeven=input('odd or even').split() #1,2

if '4' in type:
    half=input('first,second').split() #1,2


roll=random.randint(1, 36)

print('roll is ', roll)

rolldozen=math.ceil(roll/12)

if roll%2==1: rolloddeven=1
else: rolloddeven=2

if roll<19: rolllowhigh=1
else: rolllowhigh=2

#payout for type 1

if type=='1' and single==roll :
    payout=35*money
    money=money+payout
elif type=='1': money=0

#payout for type 2

if type=='2' and dozen==rolldozen :
    payout=2*money
    money=money+payout
elif type=='2': money=0

#payout fo type 3

if type=='3' and oddeven==rolloddeven :
    payout=money
    money=money+payout
elif type=='3': money=0

#payout for type 4

if type=='4' and half==rolllowhigh :
    payout=money
    money=money+payout
elif type=='4' : money=0

print('Final money is ', money)
