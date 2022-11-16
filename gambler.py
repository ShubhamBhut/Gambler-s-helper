import random
initial_capital=float(input('EnterinitialCapital:'))
winning_prob=float(input('Enterwinningprobability:'))
 
betting_amount=float(input('Enterbettingamount:'))
  
reward_ratio=float(input('Enterrisktorewardratio:'))
avg_lose=float(input('Enter averagelosefactorinloneinstance:'))
 
trade = random.choices([True, False], weights=[winning_prob, 1-winning_prob], k=2)
 
no_of_trades = int(input("Enter no. of trades: "))

for i in range no_of_trades:
    trade = random.choices([True, False], weights=[winning_prob, 1-winning_prob], k=2)
 
    if trade is True:
        current_capital = betting_amount * reward_ratio
    else:
 	    current_capital = betting_amount - (betting_amount* avg_lose)
 	
print(current_capital)

