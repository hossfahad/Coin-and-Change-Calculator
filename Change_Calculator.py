# Change and Coin Calculator
# Created by Fahad Hossain

# This program will give the exact amount of change in a transaction from how much paid and cost. 
# The change, once input, will also return it in quarters, dimes, nickels and pennies. 

# This portion of the code will calculate the change between the tender and the cost.

# This is the amount paid.
def(paid)
paid = float(raw_input("How much are you paying?: "))
# This will calculate the cost.
def(cost)
cost = float(raw_input("How much does it cost?: "))
# This will indicate the change to be received.
def(change)
change = ("paid" - "cost")
# This presents the change
print("Your change is:" change)
