#
# DSA Final Assessment Question 5 - Q5Graph.py
#
# Name : Justyn Mahen
# ID   : 21029112
#
#
import numpy as np
import pandas as pd


class Q5Graph():

    def __init__(self):
        self.maxsize = 20
        self.wmatrix = np.zeros((self.maxsize, self.maxsize), dtype=int)
        self.labels = np.zeros(self.maxsize, dtype=object)
        self.count = 0

    def addVertex(self, vname):
        if self.count == self.maxsize:
            raise Exception("Graph is full")
        if not self.hasVertex(vname):
            self.labels[self.count] = vname
            self.count += 1

    def addEdge(self, vname1, vname2, weight):
        self.addVertex(vname1)  # won't add if already there
        self.addVertex(vname2)
        label1 = self.getIndex(vname1)
        label2 = self.getIndex(vname2)
        self.wmatrix[label1, label2] = weight

    def getIndex(self, vname):  # Not on slides
        returnval = None
        for i in range(self.count):
            if self.labels[i] == vname:
                returnval = i
        return returnval

    def hasVertex(self, vname):
        returnval = False
        for v in self.labels:
            if v == vname:
                returnval = True
        return returnval

    def getVertexCount(self):
        return self.count

    # display the graph as a list
    def displayAsList(self):
        print("Vertex\tNeighbours")
        for i in range(self.count):
            print(self.labels[i], end="\t")
            for j in range(self.count):
                if self.wmatrix[i, j] != 0:
                    print(self.labels[j], end=" ")
            print()

    # Put your methods here

# 3 display methods to show movies, actors and roles
# have reused some pandas code from Question 3
# Assumption: Because the question did not specify to store the values into the graph, for the 3 individual display methods, I have
# just displayed the values after reading it from the graph

# However with displayMovieActors and displayActorsMovies, The values are stored into the graph and then displayed.

    def displaymovies(self):
        df = pd.read_csv('6degrees.csv')
        # get the first column, getting rid of duplicate movies and converting to a list which can be stored
        # into the hash table
        df = df.iloc[:, 0]
        df = df.drop_duplicates()
        print(df)

    def displayactors(self):
        df = pd.read_csv('6degrees.csv')
        df = df.iloc[:, 3]
        df = df.drop_duplicates()
        print(df)

    def displayroles(self):
        df = pd.read_csv('6degrees.csv')
        df = df.iloc[:, 5]
        df = df.drop_duplicates()
        print(df)
    # all 3 display_ methods tested in GraphTest.py using a menu, user can choose which list to display


#  display a list of all movies that an actor has appeared in


    def displayActorsMovies(self, name):
        g = Q5Graph()
        # used pandas to read the csv file and find all the movies that the actor is in
        df = pd.read_csv("6degrees.csv")
        df = df[df['Actor'].str.contains(name)]
        g.addVertex(name)
        # made the desired actor and its movies all vertexes in the graph
        for i in df["Movie"]:
            g.addVertex(i)
            g.addEdge(name, i, 1)
        print("\nActor: | Movies acted in: ")
        # print only the actor vertex which will in turn print all the movies they acted in
        for i in range(g.count):
            if g.labels[i] == name:
                print(g.labels[i], end="\t")
                for j in range(g.count):
                    if g.wmatrix[i, j] != 0:
                        print(g.labels[j], end=" ")
                print()

# display a list of all actors that have appeared in a movie
    def displayMovieActors(self, name):
        q = Q5Graph()
        # used pandas to read the csv file and find all the actors that are in the movie
        df = pd.read_csv("6degrees.csv")
        df = df[df['Movie'].str.contains(name)]
        # made the desired movie and its actors all vertexes in the graph
        for i in df["Actor"]:
            q.addVertex(i)
            q.addEdge(name, i, 1)
        print("\nMovie: | Actors in the movie: ")
        # print only the movie vertex which will in turn print all the actors in the movie
        for i in range(q.count):
            if q.labels[i] == name:
                print(q.labels[i], end="\t")
                for j in range(q.count):
                    if q.wmatrix[i, j] != 0:
                        print(q.labels[j], end=" ")
                print()
