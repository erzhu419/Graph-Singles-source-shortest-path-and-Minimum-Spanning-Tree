# Given a graph and a source vertex in graph, find shortest paths from source to all vertices in the given graph
from collections import defaultdict
import sys
import time

class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def addEdge(self, frm, to, weight):
        self.graph[frm].append([to, weight])

        if self.directed is False:
            self.graph[to].append([frm, weight])
        elif self.directed is True:
            self.graph[to] = self.graph[to]

    def find_min(self, dist, visited):
        minimum = float('inf')
        index = -1
        for v in self.graph.keys():
            if visited[v] is False and dist[v] < minimum:
                minimum = dist[v]
                index = v

        return index

    def dikstra(self, src):
        visited = {i: False for i in self.graph}
        dist = {i: float('inf') for i in self.graph}
        parent = {i: None for i in self.graph}

        dist[src] = 0

        # find shortest path for all vertices
        for i in range(len(self.graph) - 1):
            u = self.find_min(dist, visited)
            visited[u] = True
            for v, w in self.graph[u]:

                if visited[v] is False and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    parent[v] = u
        return parent, dist

    def printPath(self, parent, v):
        if parent[v] is None:
            return
        self.printPath(parent, parent[v])
        print(chr(v+65),end=" ")

    def printSolution(self, dist, parent, src):
        print('{}\t{}\t{}'.format('Vertex', 'Distance', 'Path'))

        for i in self.graph.keys():
            if i == src:
                continue
            if  dist[i]==float("inf"):
                continue
            print('{} -> {}\t\t{}\t\t{}'.format(chr(src+65), chr(i+65), dist[i], chr(src+65)), end=' ')
            self.printPath(parent, i)
            print()

# Input program
count=0
print("---------------------------------------------------------------")
#graph=None
directed=False
while(count<4):
    f1 = open("input"+str(count)+".txt","r")

    i=0
    src=sys.maxsize
    print()
    print('\033[1m'+"Shortest paths for the input file",
        "input" + str(count) + ".txt"+'\033[0m')
    print()


    for line in f1.readlines():

        x = line.split()
        #print("x",x)
        if i==0:
            no_of_vertices=int(x[0])
            print('Number of Vertices in the graph:',no_of_vertices)
            print('Number of Edges in the graph:', int(x[1]))
            dir = x[2]
            if dir=="U":
                directed = False
            else:
                directed=True
            graph=Graph(directed)

        elif len(x)==1:
            src=ord(x[0])-65
        else:
            #print(ord(x[0])-65,ord(x[1])-65,int(x[2]))
            graph.addEdge(ord(x[0])-65,ord(x[1])-65,int(x[2]))
        i=i+1
    print("Source:",chr(src+65))
    if dir=="U":

        print("The Graph is "+""+'\033[1m'+"UNDIRECTED"+'\033[0m')
    elif dir=="D":
        print("The Graph is"+" "+'\033[1m'+ "DIRECTED"+'\033[0m')

    start_time = time.time()
    parent, dist = graph.dikstra(src)
    graph.printSolution(dist, parent, src)
    runtime = (time.time() - start_time) * 1000
    print('======================================================================')
    print('Time elapsed for running Dijkstras Algorithm in Microseconds:',runtime)
    print('======================================================================')
    print()
    count+=1
    print("********************************************************************")
    print('\t')
