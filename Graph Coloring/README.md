# Visualisation of Graph Coloring Problem using networkx library

### Graph Coloring ###

 Graph Coloring Problem is an NP complete problem where "colors" are assigned to elements of a graph(edge ,node or face) subject to certain constraints.

 This is an illustration of Vertex Coloring problem. The problem is that, given an undirected graph, assign colors to each node such that no two ajacent nodes have the same color. It also involves minimization of the number of colors used.

 Basic approach:

 Step 1: Assign first color to the first vertex
 Step 2: For each of the remaining vertices, color the vertex with the lowest numbered color which has not yet been used for any of its neighbouring vertices.

 The above approach is a Greedy approach. It doesn't guarantee to use minimum number of color's each time. One way to improve this is by ordering the vertices in the decreasing order of their valency. And apply node coloring in that order. By doing so, the node with maximum color conflicts will be resolved first, and hence works better. This is Welsh - Powell algorithm.


#### Working ####

For the sample input below:

```
16
0 7
0 1
1 3
3 2
3 8
3 10
7 8
7 9
7 10
7 6
8 9
9 10
6 5
10 4
5 4
6 10
```
Visualization of the input graph:

![1](https://user-images.githubusercontent.com/22571531/28072420-93b63840-6670-11e7-8178-45c47e8fddfe.png)


Visualization of the result after node coloring.                                                  
Following 4 colors have been used:                                                          
Blue : 0, 3, 5                                                              
Purple : 1, 2, 4, 6, 9                                                              
Green : 7                                                                  
Yellow : 8, 10                                                        

![2](https://user-images.githubusercontent.com/22571531/28072424-9638f80a-6670-11e7-99ba-7b83ab92193c.png)

#### Complexity ####

Time: O(N^2 + E)                                                                                                          
N - number of Nodes                                              
E - number of Edges                                               



 



