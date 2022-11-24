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

rolldozen=str(math.ceil(roll/12))

if roll%2==1: rolloddeven=1
else: rolloddeven=2

if roll<19: rolllowhigh=1
else: rolllowhigh=2

rolloddeven = str(rolloddeven)
rolllowhigh = str(rolllowhigh)
#payout for type 1

if '1' in type and single==roll :
    payout=35*money
    money=money+payout
elif '1' in type: money=0

#payout for type 2

if '2' in type:
    payout = (dozen.count(rolldozen) * 2 * money) - ((len(dozen)-dozen.count(rolldozen)) * money)
    money=money+payout

#payout fo type 3

if '3' in type and oddeven==rolloddeven :
    payout=money
    money=money+payout
elif '3' in type: money=0

#payout for type 4

if '4' in type and half==rolllowhigh :
    payout=money
    money=money+payout
elif '4' in type : money=0

print('Final money is ', money)
print('Type is: ', type)
print('dozen is: ', dozen)
print(rolldozen)
