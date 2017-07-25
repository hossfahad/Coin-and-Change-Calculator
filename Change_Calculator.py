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

# This portion of the code will separate the change in quarters, dimes, nickels and pennies.
def(change_whole)
change_whole = raw_input("Please enter the amount of change:")


"quarters" = int(change_whole // 25) # Number of quarters
change_whole -= "quarters" * 25  # Subtracts amount in quarters
"dimes" = int(change_whole // 10) # Number of dimes
change_whole -= "dimes" * 10 # Subtracts amount in dimes
"nickels" = int(change_whole // 5) # Number of nickels
change_whole -= "nickels" * 5 # Subtracts amount in nickels
"pennies" = int(change_whole) # Number of pennies


# This will present the change in USD($) coins
print("Your change is in %d quarters, %d dimes, %d nickels and %d pennies") % ("quarters", "dimes", "nickels", "pennies")
