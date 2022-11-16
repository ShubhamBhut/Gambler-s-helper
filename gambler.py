<<<<<<< HEAD
initial_capital = float(input('Enter initial Capital: '))

winning_prob = float(input('Enter winning probability: '))

betting_amount = float(input('Enter betting amount: '))

reward_ratio = float(input('Enter reward ratio: '))

avg_lose = float(input('Enter average lose factor in one instance: '))

if trade == win

#current_capital = betting_amount*((1+reward_ratio)**winning_prob)*((1-avg_lose)**(1-winning_prob))

print(current_capital)
=======
 
import random
initial_capital=float(input('EnterinitialCapital:'))
winning_prob=float(input('Enterwinningprobability:'))
 
betting_amount=float(input('Enterbettingamount:'))
  
reward_ratio=float(input('Enterrisktorewardratio:'))
avg_lose=float(input('Enter averagelosefactorinloneinstance:'))
 
trade = random.choices([True, False], weights=[winning_prob, 1-winning_prob], k=2)
 
if trade is True:
    current_capital = betting_amount * reward_ratio
else:
 	current_capital = betting_amount - (betting_amount* avg_lose)
 	
print(current_capital)

>>>>>>> 7520e9f6bb010b24db972d4d7c7981af0388663e
