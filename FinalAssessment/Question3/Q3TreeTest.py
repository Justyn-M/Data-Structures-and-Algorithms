#
# DSA Final Assessment Question 3 - Q3TreeTest.py
#
# Name : Justyn Mahen
# ID   : 21029112
#
#
from Q3BSTree import *

print("\n##### Question 3: Testing Trees #####\n")

# Put your code here
t = Q3BSTree()

choice = input(
    "Do you want to see the list of (M)ovies, (A)ctors or (R)oles? ")
if choice == "M":
    t.storeMovies()
elif choice == "A":
    t.storeActors()
elif choice == "R":
    t.storeRoles()
else:
    print("Invalid input")

print("\n##### Tests Complete #####\n")
