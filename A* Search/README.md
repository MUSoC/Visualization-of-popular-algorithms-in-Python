# Visualisation of A* Search using networkx library

### A* Search ###

A* search( pronounced as "A star") is a search algorithm which explores a graph by expanding the that node which minimizes steps from the source(like in BFS) as well as approximate steps to the goal(like in greedy bfs). Hence, this algorithm is thorough and fast as it combines the strengths of both BFS and Greedy BFS.
A* algorithm is proven to give the optimal solution to a problem.

What is the evaluation function here?

Evaluation function-f is the criterion based on which the next node is chosen. 
f is the sum of 2 parameters:
1. cost of path from source to the given node
2. approximate cost of reaching the goal from the given node (heuristic function)
So, at each step, the node is chosen such that sum of the above 2 parameters, that is, f is minimal. 

