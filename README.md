# Graph-Singles-source-shortest-path-and-Minimum-Spanning-Tree
## Dijkstra’s shortest path algorithm
Djikstra's algorithm(named after its discover,E.W Dijkstra) is a greedy method which used for finding the shortest path from a particular node in a graph (source node) to the destination. This algorithm finds the shortest distance from a source vertex s in V given the graph G= (V,E) to every vertex in V,hence this problem is sometimes called the single-source shortest paths problem.
Assumption:
Graphs are connected.
Edges are undirected or directed.
Edge weights are non negative.

### Below are the steps for finding MST using Dijkstra’s algorithm:
1.Built a graph using adj list for all the edges and their weight based on the graph is directed or undirected for all the 4 inputs.
2.Created a shortest path tree set called visited that keeps track of vertices included in shortest path tree
3.Assigned a distance value to all vertices in the input graph. Initialized all distance values as infinite in the starting and  distance value as 0 for the source vertex so that it should be picked first.
4.Created a data structure for parent which keep track of path followed and used to display in the output.
5.Until “visited” does not included all vertices, a vertex with the minimum distance value has been picked and added to visited.The distance value of all the adjacent vertices has been updated.
 

### Problem 1:
Find shortest paths in both directed and undirected weighted graphs for a given source vertex. Assume there is no negative edge in your graph. You will print each path and path cost for a given source. 
### Runtime and Data Structure:
We have used defaultdict to build a adj list to represent graph for this algorithm.Time Complexity of the this implementation implementation is O(V2) . As the relaxation of vertex happens for the minimum picked vertex weight.So this step will take O(V2) Runtime.








## Kruskal's Algorithm
Given a connected and undirected graph, a spanning tree of that graph is a subgraph that is a tree and connects all the vertices together. There can be many different spanning trees for a single graph .
A minimum spanning tree (MST) od minimum weight spanning tree for a weighted, connected and undirected graph is a spanning tree with weight less than or equal to the weight of every other spanning tree. 
The weight of a spanning tree is the sum of weights given to each edge of the spanning tree. A minimum spanning tree has (V – 1) edges where V is the number of vertices in the given graph.
Kruskal’s Algorithm builds the spanning tree by adding edges one by one into a growing spanning tree. Kruskal's algorithm is a greedy approach algorithm.It is such because in each  iteration a least weight is found and is added to the growing spanning tree.

### Below are the steps for finding MST using Kruskal’s algorithm
Built a graph using adj list for all the edges and their weight.
Edges has been sorted in non decreasing order of their weight
The smallest edge has been picked and checked if it forms a cycle with the spanning tree formed till now.If the cycle is not formed ,included the edges.
Repeat step#2 until there are (V-1) edges in the spanning tree. 

### Problem 2:
Given a connected, undirected, weighted graph, find a spanning tree using edges that minimizes the total weight 𝑤 𝑇 = (),*)∈, 𝑤(𝑢, 𝑣). Use Kruskal or Prims algorithm to find Minimum Spanning Tree (MST).

### Data Structure and Runtime Analysis :
O(E logE) or O(E logV). Sorting of edges takes O(ELogE) time. After sorting, we
iterate through all edges and apply find-union algorithm. The find and union
operations can take atmost O(LogV) time. So overall complexity is O(ELogE +
ELogV) time. The value of E can be atmost O(V2), so O(LogV) are O(LogE)
same. Therefore, overall time complexity is O(ElogE) or O(ElogV).
