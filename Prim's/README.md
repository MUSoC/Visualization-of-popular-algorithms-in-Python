# Visualisation of Prim's algorithm using networkx library

### INPUT ###


Input is taken from the file 
#### input.txt ####

Sample input
```
  5
  0 2 7 -1 -1
  -1 0 3 8 5
  -1 2 0 1 -1
  -1 -1 -1 0 4
  -1 -1 -1 5 0

```
First line contains the number of nodes,say n.(Nodes are numbered as 0,1,2,...(n-1) )
Followed by n*n weighted matrix. Disconnected egdes are represented by negative weight.

### Draw Graph ###


Graph is first drawn from the weighted matrix input from the user with weights shown. Edges are marked with black.



### Prim's algorithm ###

Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for
a weighted undirected garph. 

Here, starting from an arbitrary node, the algorithm operates by building this tree one vertex at a time. At each step, smallest egde connection (also known as cut) from the tree to another vertex is added to the resulting tree.

To understand this better, consider the above input.
Let the arbitrary starting node be 0.

The graph, initially.

![1](https://user-images.githubusercontent.com/22571531/27260081-d03f8c7c-5440-11e7-8119-5b61fb32daee.png)

We use the following 3 lists:

#### dist ####
 dist[i] will hold the minimum weight edge value of node i to be included in MST(Minimum Spanning Tree).                               
#### parent ####                               
parent[i] will hold the vertex connected to i, in the MST edge.                          
#### mstSet ####                         
mstSet[i] will hold true if vertex i is included in the MST.                           

#### Initial values: ####
```
dist   = [0, inf ,inf, inf, inf]
parent = [-1, None, None, None]                        
mstSet = [True, False, False, False, False]
```

#### After the first iteration: ####

Node 1 and Node 2 form an edge with the starting node,i.e, 0 with a distance of 2 and 7 respectively. Hence they are updated accordingly.

```
dist   = [0, 2, 7, inf, inf]
parent = [-1, 0, 0, None, None] 
mstSet = [True, False, False, False, False]
```

Minimum most edge value of the nodes which are not included in the MST yet, i.e, where mstSet[i] == False, is node 1.
The node is now included in the MST, and thus, mstSet[1] is set to True.

![2](https://user-images.githubusercontent.com/22571531/27260083-d420d896-5440-11e7-96a1-db6b545e351c.png)


#### After the second iteration: ####

```
dist   = [0, 2, 3, 8, 5]
parent = [-1, 0, 1, 1, 1]
mstSet = [True, True, False, False, False]
```

![3](https://user-images.githubusercontent.com/22571531/27260084-d71199f0-5440-11e7-9bd5-d62c3f494ec7.png)

#### After the third iteration: ####

```
dist   = [0, 2, 3, 1, 5]
parent = [-1, 0, 1, 2, 1]
mstSet = [True, True, True, False, False]
```

![4](https://user-images.githubusercontent.com/22571531/27260085-da745fc4-5440-11e7-817b-75e771bb765f.png)

#### After the fourth iteration: ####

```
dist   = [0, 2, 3, 1, 4]
parent = [-1, 0, 1, 2, 3]
mstSet = [True, True, True, True, False]
```

Here, the red edges denote the Minimum Spanning Tree

![5](https://user-images.githubusercontent.com/22571531/27260088-dde230be-5440-11e7-83ce-6e95b228c7d7.png)