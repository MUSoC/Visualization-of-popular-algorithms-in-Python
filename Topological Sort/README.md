# Visualisation of Topological sort algorithm using networkx library

### Topological sort ###

 Topological sort of a directed graph is a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering. For instance, the vertices of the graph may represent tasks to be performed, and the edges may represent constraints that one task must be performed before another; in this application, a topological ordering is just a valid sequence for the tasks.
 PS: Topological sorting is possible only if the graph is a directed acyclic graph.

 Two commom approaches for topological sort:
 1. Kahn's algorithm
 2. Depth - first search

 The code here is an implementation of Kahn's algorithm.
