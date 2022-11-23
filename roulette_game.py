import random
import math

money=input('')
type=input('type of bet, for single enter 1, for 12 enter 2, for odd/even enter 3, for high/low, enter 4: ')


if type==1:
    single=input('bet on') #1-36

if type==2:
    dozen=input('first,second,third') #1,2,3

if type==3:
    oddeven=input('odd or even') #1,2

if type==4:
    half=input('first,second') #1,2


roll=random.randint(1, 36)

print(roll)

rolldozen=math.ceil(roll/12)

if roll%2==1: rolloddeven=1
else: rolloddeven=2

if roll<19: rolllowhigh=1
else: rolllowhigh=2

#payout for type 1

if type==1 and single==roll :
    payout=35*money
    money=money+payout
elif type==1: money=0

#payout for type 2

if type==2 and dozen==rolldozen :
    payout=2*money
    money=money+payout
elif type==2: money=0

#payout fo type 3

if type==3 and oddeven==rolloddeven :
    payout=money
    money=money+payout
elif type==3: money=0

#payout for type 4

if type==4 and half==rolllowhigh :
    payout=money
    money=money+payout
elif type==4 : money=0
