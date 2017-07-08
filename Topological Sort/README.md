# Visualisation of Topological sort algorithm using networkx library

### Topological sort ###

 Topological sort of a directed graph is a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering. For instance, the vertices of the graph may represent tasks to be performed, and the edges may represent constraints that one task must be performed before another; in this application, a topological ordering is just a valid sequence for the tasks.
 PS: Topological sorting is possible only if the graph is a directed acyclic graph.

 Two commom approaches for topological sort:
 1. Kahn's algorithm
 2. Depth - first search

 The code here is an implementation of Kahn's algorithm.

 #### Kahn's algorithm ####

 This is computationally simpler compared to DFS approach.

 Step 1: Find all the nodes in the graph with in-degree as 0 and add them into a queue
 Step 2: Remove the nodes from the queue one by one, append it to the sorted_list and simulatneously update the graph(remove the node from the graph, resulting which, in-degree of nodes which had edges directed from the reomved node decreases by one).
 Step 3: If there are anymore nodes left in the graph, go back to step 1 

 This method is optimal but modifies the graph. For the algorithm to not modify the original graph, you'll need to maintain a boolean array visited[] - to keep track to the visited nodes and indegree[] to store the in-degree of the graph nodes.

#### Working ####

Consider the sample input below:

```
6
1 2
1 3
2 3
2 4
3 4
3 5
```
Visualization of the input graph:

![1](https://user-images.githubusercontent.com/22571531/27983933-e09f086c-63e6-11e7-9830-b63a48b829b6.png)


Node 1 is the only node with in-degree as 0.
Remove it from the graph, and append it to the sorted_list.
sorted_list = [1]

Now, Node 2 has an in-degree of 0. Remove it from the graph, and append it to the sorted list.
sorted_list = [1,2]

Next, Node 3 has an in-degree of 0. 
sorted_list = [1,2 3]

Next, Node 4 and Node 5, both have an in-degree of 0.
sorted_list = [1,2,3,4,5]
Note that: [1,2,3,5,4] is also the right order.

Visualization of the topologically sorted order.                              
Green node - denotes the starting node.                                      
Red node - denotes the final node.

![2](https://user-images.githubusercontent.com/22571531/27983935-e5d92286-63e6-11e7-92f3-e45c9bbb6039.png)                                                                             


 



