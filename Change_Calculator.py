# Change and Coin Calculator
# Created by Fahad Hossain
# This program will give the exact amount of change in a transaction from how much paid and cost.
# The change, once input, will also return it in quarters, dimes, nickels and pennies. 

# This portion of the code will calculate the change between the tender and the cost.

# This is the amount paid.
paid = float(input("How much are you paying?: "))
# This will calculate the cost.
cost = float(input("How much does it cost?: "))
# This will indicate the change to be received.
change = (paid - cost)
# This presents the change
print("Your change is:", ("%.2f" % change))

# This portion of the code will separate the change in quarters, dimes, nickels and pennies.
# The value of coins in USD.
hundreddollar = 10000
fiftydollar = 5000
twentydollar = 2000
tendollar = 1000
fivedollar = 500
onedollar = 100
quarter = 25
dime = 10
nickel = 5
penny = 1
coins = [10000, 5000, 2000, 1000, 500, 100, 25, 10, 5, 1]
coinNames = ["hundred dollar bills", "fifty dollar bills", "twenty dollar bills", "ten dollar bills", \
             "five dollar  bills", "one dollar bills", "quarters", "dimes", "nickels", "pennies"]

# This shows how to retrieve the change that will be separated.
paid = int(float(paid) * 100)
cost = int(float(cost) * 100)
change = paid - cost

# This portion subtracts the total once divided by a dollar, which is then divided into quarters and so on.
# Use of loop in order to divide change amongst each bill respectively. 
amts = []

for idx, value in enumerate(coins):
    amt = change // value
    change = change % value
    amts.append((int(amt), coinNames[idx]))
    
# This prints the change in their respective coin.

print("Your change will be in: ")
for amt, coin in amts:
    print(amt, coin)
