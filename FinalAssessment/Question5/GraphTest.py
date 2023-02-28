#
# DSA Final Assessment Question 5 - Q5GraphTest.py
#
# Name : Justyn Mahen
# ID   : 21029112
#
#
from Q5Graph import *


print("\n##### Question 5: Testing Graphs #####\n")

g = Q5Graph()

g.addVertex("one")
g.addVertex("two")
g.addVertex("three")
g.addVertex("four")

g.addEdge("one", "two", 3)
g.addEdge("one", "three", 4)
g.addEdge("one", "four", 5)
g.addEdge("four", "two", 6)
g.addEdge("four", "three", 7)

g.displayAsList()

choice = input('Do you want to see all (A)ctors, (M)ovies or (R)oles? ')
if choice == 'A':
    g.displayactors()
    print('### End of actors list ###')
elif choice == 'M':
    g.displaymovies()
    print('### End of movies list ###')
elif choice == 'R':
    g.displayroles()
    print('### End of roles list ###')

print("\n##### Printing all Movies a specific actor is in #####\n")
g.displayActorsMovies("Morgan Freeman")

print("\n##### Printing all Actors in a specific movie #####\n")
g.displayMovieActors("The Bucket List")

print("\n##### Tests Complete #####\n")
