# Visualisation of Kruskal's algorithm using networkx library

### INPUT ###


Input is taken from the file 
#### input.txt ####

Sample input
```
  5
  0 2 7 -1 -1
  2 0 3 8 5
  7 3 0 1 -1
  -1 8 1 0 4
  -1 5 -1 4 0

```
First line contains the number of nodes,say n.(Nodes are numbered as 0,1,2,...(n-1) )
Followed by n*n weighted matrix. Disconnected edges are represented by negative weight.

### Draw Graph ###


Graph is first drawn from the weighted matrix input from the user with weights shown. Edges are marked with black.



### Kruskal's algorithm ###

Kruskal's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected garph. 

The algorithm operates by adding the egdes one by one in the order of their increasing lengths, so as to form a tree. Egdes are rejected if it's addition to the tree, forms a cycle. This continues till we have V-1 egdes in the tree. (V stands for the number of vertices).

To understand this better, consider the above input.

The graph, initially.

![1](https://user-images.githubusercontent.com/22571531/27430044-b959f994-5764-11e7-9b3e-aa0c10dc98e9.png)
                           

#### After the first iteration: ####

The smallest edge is of length 1, connecting Node 2 and Node 3. Since it is the first edge, it is added directly to the tree.


![2](https://user-images.githubusercontent.com/22571531/27430048-bcf86eb4-5764-11e7-8f03-397f601338b2.png)


#### After the second iteration: ####

Next smallest edge is of length 2, connecting Node 0 and Node 1. Since it's addition doesn't result in a cycle, it is added to the tree.


![3](https://user-images.githubusercontent.com/22571531/27430058-c0a1da78-5764-11e7-8a0a-a29ab5442d80.png)

#### After the third iteration: ####

Next smallest edge is of length 3, connecting Node 1 and Node 2. Since it's addition doesn't result in a cycle, it is added to the tree.

![4](https://user-images.githubusercontent.com/22571531/27430069-c607466a-5764-11e7-9a2e-7d60e5d50254.png)

#### After the fourth iteration: ####

Next smallest edge is of length 4, connecting Node 3 and Node 4. Since it's addition doesn't result in a cycle, it is added to the tree.

Now we have 4 edges, hence we stop the iteration.
Final graph, with red edges denoting the minimum spanning tree.

![5](https://user-images.githubusercontent.com/22571531/27430080-ce205b20-5764-11e7-8bca-20f452d8b20d.png)

#### Complexity ####

Time: O(V^2)                                                                 
V - Number of vertices                                          