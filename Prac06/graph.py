#
# graph.py - classes for a graph using an adjacency list
#

from linkedLists import *
from stack_queue import DSAStack, ShuffleQueue

class DSAGraphNode:
    def __init__(self, label: object, value: object):
        self._label = label
        self._value = value
        self._adjacent = DSALinkedList()
        self._visited = False

    def getLabel(self) -> object:
        return self._label

    def getValue(self) -> object:
        return self._value

    def adjacent(self) -> 'DSALinkedList':
        return self._adjacent

    def addEdge(self, node: 'DSAGraphNode') -> None:
        self._adjacent.insertLast(node)

    def visited(self) -> bool:
        return self._visited

    def setVisited(self, visited: bool) -> None:
        self._visited = bool(visited)

    def __str__(self) -> str:
        return str(self._label) + ": " + str(self._value)


class DSAGraph:
    def __init__(self):
        self._nodes = DSALinkedList()

    def addNode(self, label: object, value: object) -> 'DSAGraphNode':
        node = DSAGraphNode(label, value)
        self._nodes.insertLast(node)
        return node

    def getNode(self, label: object) -> 'DSAGraphNode':
        node = None
        for n in self._nodes:
            if n.getLabel() == label:
                node = n
                break
        return node

    def getNodes(self) -> 'DSALinkedList':
        return self._nodes

    def __str__(self) -> str:
        graphStr = ""
        for node in self._nodes:
            graphStr += str(node) + " -> "
            for adj in node.adjacent():
                graphStr += str(adj) + " "
            graphStr += " "
        return graphStr

    def depthFirstSearch(self, start: 'DSAGraphNode') -> 'DSALinkedList':
        stack = DSAStack()
        visited = DSALinkedList()
        stack.push(start)
        while not stack.isEmpty():
            node = stack.pop()
            if not node.visited():
                node.setVisited(True)
                visited.insertLast(node)
                for adj in node.adjacent():
                    stack.push(adj)
        return visited

    def breadthFirstSearch(self, start: 'DSAGraphNode') -> 'DSALinkedList':
        queue = ShuffleQueue()
        visited = DSALinkedList()
        queue.enqueue(start)
        while not queue.isEmpty():
            node = queue.dequeue()
            if not node.visited():
                node.setVisited(True)
                visited.insertLast(node)
                for adj in node.adjacent():
                    queue.enqueue(adj)
        return visited

    def resetVisited(self) -> None:
        for node in self._nodes:
            node.setVisited(False)

    # read a graph from a file and return the graph
    def readGraph(self, filename: str) -> 'DSAGraph':
        graph = DSAGraph()
        file = open(filename, "r")
        for line in file:
            line = line.strip()
            if line != "":
                line = line.split()
                node = graph.addNode(line[0], line[1])
                for i in range(2, len(line)):
                    adj = graph.getNode(line[i])
                    node.addEdge(adj)
        file.close()
        return graph


# test the code
if __name__ == "__main__":
    print('Creating new graph...')
    print('Adding nodes...')
    print('Adding edges...')
    print('Printing graph...')
    print('=====================')
    graph = DSAGraph()
    a = graph.addNode("A", 1)
    b = graph.addNode("B", 2)
    c = graph.addNode("C", 3)
    d = graph.addNode("D", 4)
    e = graph.addNode("E", 5)
    f = graph.addNode("F", 6)
    g = graph.addNode("G", 7)
    h = graph.addNode("H", 8)
    i = graph.addNode("I", 9)
    j = graph.addNode("J", 10)
    k = graph.addNode("K", 11)
    l = graph.addNode("L", 12)
    m = graph.addNode("M", 13)
    n = graph.addNode("N", 14)
    o = graph.addNode("O", 15)
    p = graph.addNode("P", 16)
    q = graph.addNode("Q", 17)
    r = graph.addNode("R", 18)
    s = graph.addNode("S", 19)
    t = graph.addNode("T", 20)
    u = graph.addNode("U", 21)
    v = graph.addNode("V", 22)
    w = graph.addNode("W", 23)
    x = graph.addNode("X", 24)
    y = graph.addNode("Y", 25)
    z = graph.addNode("Z", 26)
    a.addEdge(b)
    a.addEdge(c)
    a.addEdge(d)
    b.addEdge(e)
    b.addEdge(f)
    c.addEdge(g)
    c.addEdge(h)
    d.addEdge(i)
    d.addEdge(j)
    e.addEdge(k)
    e.addEdge(l)
    f.addEdge(m)
    f.addEdge(n)
    g.addEdge(o)
    g.addEdge(p)
    h.addEdge(q)
    h.addEdge(r)
    i.addEdge(s)
    i.addEdge(t)
    j.addEdge(u)
    j.addEdge(v)
    k.addEdge(w)
    k.addEdge(x)
    l.addEdge(y)
    l.addEdge(z)
    print(graph)
    print("Depth First Search:")
    print('=====================')
    for node in graph.depthFirstSearch(a):
        print(node)
    graph.resetVisited()
    print("Breadth First Search:")
    print('=====================')
    for node in graph.breadthFirstSearch(a):
        print(node)
    graph.resetVisited()
    print('Reading graph 1 from file...')
    print('============================')
    # test reading a graph from a file
    graph = graph.readGraph("prac6_1.al")
    print(graph)
    print('Reading graph 2 from file...')
    print('============================')
    graph = graph.readGraph("prac6_2.al")
    print(graph)
