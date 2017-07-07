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
 Step 3: If there are anymore nodes left in the graph, go to step 1 

 This method is optimal but modifies the graph. For the algorithm to not modify the original graph, you'll need to maintain a boolean array visited[] - to keep track to the visited nodes and indegree[] to store the in-degree of the graph nodes.


 



