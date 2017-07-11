# Visualisation of Graph Coloring Problem using networkx library

### Graph Coloring ###

 Graph Coloring Problem is an NP complete problem where "colors" are assigned to elements of a graph(edge ,node or face) subject to certain constraints.

 This is an illustration of Vertex Coloring problem. The problem is that, given an undirected graph, assign colors to each node such that no two ajacent nodes have the same color. It also involves minimization of the number of colors used.

 Basic approach:

 Step 1: Assign first color to the first vertex
 Step 2: For each of the remaining vertices, color the vertex with the lowest numbered color which has not yet been used for any of its neighbouring vertices.

 The above approach is a Greedy approach. It doesn't guarantee to use minimum number of color's each time. One way to improve this is by ordering the vertices in the decreasing order of their valency. And apply node coloring in that order. By doing so, the node with maximum color conflicts will be resolved first, and hence works better. This is Welsh - Powell algorithm.






 



