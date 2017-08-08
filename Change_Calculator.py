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

# This shows how to retrieve the change that will be separated.
paid = int(float(paid) * 100)
cost = int(float(cost) * 100)
change = paid - cost

# This portion subtracts the total once divided by a dollar, which is then divided into quarters and so on.
ffdb = change // fiftydollar
ffdbpartialchange = change - ffdb * fiftydollar
twdb = ffdbpartialchange // twentydollar
twdbpartialchange = ffdbpartialchange - twdb * twentydollar
tdb = twdbpartialchange // tendollar
tdbpartialchange = twdbpartialchange - tdb * tendollar
fdb = tdbpartialchange // fivedollar
fdbpartialchange = change - fdb * fivedollar
sdb = fdbpartialchange // onedollar
sdbpartialchange = change - sdb * onedollar
qb = sdbpartialchange // quarter
qpartialchange = sdbpartialchange - qb * quarter
db = qpartialchange // dime
dpartialchange = qpartialchange - db * dime
nb = dpartialchange // nickel
npartialchange = dpartialchange - nb * nickel
pb = npartialchange // penny
ppartialchange = npartialchange - pb * penny

# This prints the change in their respective coin.
print("Your change will be in: %s fifty-dollar notes, %s twenty-dollar notes, %s ten-dollar notes, %s five-dollar notes, %s single-dollar notes, %s quarters, %s dimes, %s nickels and %s pennies" % (ffdb, twdb, tdb, fdb, sdb, qb, db, nb, pb))
hange is in %s quarters, %s dimes, %s nickels and %s pennies" % qb, db, nb, pb))
