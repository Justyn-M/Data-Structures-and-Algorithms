#
# DSA Final Assessment Question 3 - Q3HashTest.py
#
# Name : Justyn Mahen
# ID   : 21029112
#
#
from Q3HashTable import *

print("\n##### Question 3: Testing Hash Tables #####\n")

tab = Q3HashTable(20)
data = ["11111110", "11111101", "11111011", "11110111",
        "11101111", "11011111", "10111111", "01111111"]
print("Table size is: " + str(tab.getArrayLength()))

for i in range(0, len(data)):
    tab.put(data[i], "O"+data[i])

tab.display()
print("Load Factor is: " + str(tab.getLoadFactor()))

### User Menu ###
choice = input(
    "Do you want to see the list of (M)ovies, (A)ctors or (R)oles? ")
if choice == "M":
    tab.storeMovies()
elif choice == "A":
    tab.storeActors()
elif choice == "R":
    tab.storeRoles()
else:
    print("Invalid input")


print("\n##### Tests Complete #####\n")
