import random
initial_capital=float(input('Enter initial Capital:'))
winning_prob=float(input('Enter winning probability:'))
 
betting_amount=float(input('Enter betting-amount:'))
  
reward_ratio=float(input('Enter reward ratio:'))
avg_lose=float(input('Enter average lose-factor in one instance:'))
 
trade = random.choices([True, False], weights=[winning_prob, 1-winning_prob], k=1)
 
no_of_trades = int(input("Enter no. of trades: "))

for i in range(no_of_trades):
    trade = random.choices([True, False], weights=[winning_prob, 1-winning_prob], k=1)
 
    if trade is True:
        current_capital = betting_amount * reward_ratio
    else:
 	    current_capital = betting_amount - (betting_amount* avg_lose)
 	
print(current_capital)

