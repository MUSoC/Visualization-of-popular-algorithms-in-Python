# Visualisation of Travelling Salesman Problem using networkx library

### Travelling Salesman Problem ###

Travelling salesman problem is a NP hard problem. Given a set of cities and the distance between every pair of cities, the problem is to find the shortest possible route that visits each city exactly once and returns back to the original city. Hence, it also belongs to the class of optimization problems. 

#### Why NP-hard?

First, let us understand the definition of NP- hard.
NP (nondeterministic polynomial time) problem is the one whose solution could be verified in polynomial time but the problem is not guaranteed to be solved in polynomial time.
Now, NP - hard problem are those which are atleast as hard as any NP problem.
NP complete problem is the class of problems that are both NP and NP-hard.

Let us now check both the conditions.

 ##### condition (i): NP
  To check that given solution is the right solution for a TSP problem. We need to verify two things:
  Firstly, each city must be visited exactly once. (could be done in polynomial time)
  Secondly, there is no shorter route than the current solution. (This cannot be guaranteed in polynomial time)
  Hence, TSP is not NP

 ##### condition (ii): NP hard
 Surely TSP is a NP hard problem. (For, even it's solution can't be guaranteed in polynomial time)

 Thus, TSP belongs to the class of NP-hard problem and not NP-complete.


Brute force approach for TSP will need all possible paths to be calculated which is (n-1)! paths( where n is the number of cities). As n increases, it is computationally not feasible to compute that many paths.

There are certain approximation algorithms for TSP which guarantees to solve the problem in polynomial time at the cost of solution not being exact. Christofides algorithm, is one such heuristics approach which guarantees it's solution to be within a factor of 1.5 of the optimal solution. By far, Christofides algorithm (time complexity : O(n^3)) is known to have the best approximation ratio for a general TSP problem. 

#### Christofides algorithm:

1. Create a minimum spanning tree MST of G. (using Kruskal's or Prim's algorithm)
2. Let odd_vert be the set of vertices with odd degree in MST. The number of vertices with odd_degree is guaranteed to be even( Proof: Handshaking Lemma).
3. Find a minimum-weight perfect matching pairs in the induced subgraph given by the vertices from odd_vert. Add those edges to MST.
 The resulting MST now has all the vertices with even degree- hence, is a Eulerian circuit.
4. Make the circuit found in previous step into a Hamiltonian circuit by skipping repeated vertices.

The code here,is an implementation of Christofides algorithm. 

### INPUT ###


Input is taken from the file 
#### input.txt ####

Sample input
```
5
0 10 8 9 7
10 0 10 5 6
8 10 0 8 9
9 5 8 0 6
7 6 9 6 0

```
First line contains n, the number of cities.
Followed by n*n distance matrix where matrix[i][j] denotes the distance between city i and city j.


### Draw Graph ###


An undireced graph is drawn with nodes representing the cities and egde labels denoting the distance between them.

![screenshot from 2017-06-29 12-50-58](https://user-images.githubusercontent.com/22571531/27676532-f2af862a-5ccb-11e7-9ba3-8a9cb87adca9.png)

Step 1:

A minimum spanning tree MST is obtained from the given grapg G (using Kruskal's algorithm)

![screenshot from 2017-06-29 12-53-47](https://user-images.githubusercontent.com/22571531/27676537-f787e962-5ccb-11e7-8da7-e48e223d33a8.png)

Step 2:

There are 2 vertices with odd degree in MST graph, that is, node 2 and node 3.
Hence, odd_vert = [2,3]

Step 3:

Since there are only 2 vertices in odd_vert, we get one minimum weight matching pair, i,e, (2,3). Adding this edge to MST, we have the below graph.

![screenshot from 2017-06-29 12-48-48](https://user-images.githubusercontent.com/22571531/27676543-fb8d0d76-5ccb-11e7-93b9-bc7d6767b24d.png)


Step 4:

Finding the shortest hamiltonian circuit from the above graph (by skipping already visisted vertices) , we have
```
0 -> 2 -> 3 -> 1 -> 4 -> 0
```

The below diagram shows the shortest route for TSP. 
PS: The arrows here are just for visual purposes to denote the route. The cycle could be traversed in any direction.

![second](https://user-images.githubusercontent.com/22571531/27676549-01632fc8-5ccc-11e7-964e-eece9960b4b8.png)

#### Complexity ####

Time: O(n^3)                                                          
n - number of Nodes