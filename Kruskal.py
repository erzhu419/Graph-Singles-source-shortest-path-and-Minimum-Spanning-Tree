import time

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []


    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):

        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root

        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def KruskalMST(self):

        result = []
        e = 0
        i = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:

            u, v, w = self.graph[i]

            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        print('\033[1m' + "Edge Selected \t Weight" + '\033[0m')
        print()
        res=0
        for u, v, weight in result:
            print(chr(u + 65), "-", chr(v + 65), "\t\t\t", weight)
            res+=weight
        print('\033[1m'+"The total Cost for Minimum Spanning Tree is", res,'\033[0m')


# input
print("---------------------------------------------------------------")
count = 0
print()
while (count < 4):
    print(
        '\033[1m' + "The Minimum Spanning Tree using Kruskal's Algorithm for Connected, Undirected, Weighted graph for the input file",
        "input" + str(count) + ".txt" + '\033[0m')
    print()
    f1 = open("input" + str(count) + ".txt", "r")

    i = 0
    for line in f1.readlines():
        x = line.split()
        #print("x",x)
        if i == 0:
            no_of_vertices = int(x[0])
            #print("no_of_vertices",no_of_vertices)
            graph = Graph(no_of_vertices)
        elif len(x) == 1:
            pass
        else:
            graph.addEdge(ord(x[0]) - 65, ord(x[1]) - 65, int(x[2]))
        i = i + 1
    start_time = time.time()
    graph.KruskalMST()
    runtime = (time.time() - start_time) * 1000
    print('======================================================================')
    print('Time elapsed for running Kruskal Algorithm in Microseconds:', runtime)
    print('======================================================================')
    print()
    count += 1
    print("********************************************************************")
    print('\t')


