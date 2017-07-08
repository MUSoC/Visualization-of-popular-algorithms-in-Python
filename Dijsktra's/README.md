# Visualisation of Dijsktra's algorithm using networkx library

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
  0


```
First line contains the number of nodes,say n.(Nodes are numbered as 0,1,2,...(n-1) )
Followed by n*n weighted matrix. Disconnected egdes are represented by negative weight.
Last line contains the source node.(i.e, the node from which the rest of the nodes should be reached)

### Draw Graph ###


Graph is first drawn from the weighted matrix input from the user with weights shown. Edges are marked with black.



### Dijsktras algorithm ###

DDijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph. 

Here, given the source node, the algorithm finds the shortest path from the source node to each of the remaining nodes. 

To understand this better, consider the above input.
Source node is 0.

The graph, initially.

![1](https://user-images.githubusercontent.com/22571531/27195526-ca5dd872-5224-11e7-9b34-e669c7082a6e.png)

We use the following 3 lists:

#### dist ####
 dist[i] will hold the shortest distance from source to i.                                 
#### parent ####                               
parent[i] will hold the node from which node i is reached to, in the shortest path from source.                          
#### sptSet ####                         
sptSet[i] will hold true if vertex i is included in shortest path tree.                           

#### Initial values: ####
```
dist   = [0, inf ,inf, inf, inf]
parent = [-1, None, None, None]                        
sptSet = [True, False, False, False, False]
```

#### After the first iteration: ####

Node 1 and Node 2 can be reached directly from source node,i.e, 0 with a distance of 2 and 7 respectively. Hence they are updated accordingly.

```
dist   = [0, 2, 7, inf, inf]
parent = [-1, 0, 0, None, None] 
sptSet = [True, False, False, False, False]
```

Minimum most distance of those where sptSet[i] == False, is node 1.
Hence, the node is now included in the shorted path tree, hence sptSet[1] is set to True.

![2](https://user-images.githubusercontent.com/22571531/27195530-cd783296-5224-11e7-87f5-a404a94fed84.png)


#### After the second iteration: ####

```
dist   = [0, 2, 5, 10, 7]
parent = [-1, 0, 1, 1, 1]
sptSet = [True, True, False, False, False]
```

![3](https://user-images.githubusercontent.com/22571531/27195531-d081e824-5224-11e7-8993-81f2dc43c30f.png)

#### After the third iteration: ####

```
dist   = [0, 2, 5, 6, 7]
parent = [-1, 0, 1, 2, 1]
sptSet = [True, True, True, False, False]
```

![4](https://user-images.githubusercontent.com/22571531/27195536-d310f896-5224-11e7-8a75-eb5e883bc37b.png)

#### After the fourth iteration: ####

```
dist   = [0, 2, 5, 6, 7]
parent = [-1, 0, 1, 2, 1]
sptSet = [True, True, True, True, False]
```

Here, the red edges denote the shortest path from source node to the rest of the nodes.

![5](https://user-images.githubusercontent.com/22571531/27195545-d8cfdf68-5224-11e7-8ee9-1b2d38e1d6ad.png)

#### Complexity ####
Time : O(V^2)                                                           
V - number of Vertices                                
