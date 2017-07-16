# Visualisation of K - Centers Problem using networkx library

### K - Center ###

 K - Center problem (also known as Metric K - Center problem) is a NP - Hard Problem where given n cities, one needs to choose k (k<=n) centers, such that maximum distance of a city to the center is minimized. 

 In layman terms,say we need to bulid k warehouses given a map of n connected cities. The best way to build a warehouse, is by keeping in mind that, it must be closest to the cities. In other words, the maximum distance of a city to the warehouse must be minimal.


 Greedy approach:

 Here, is an illustration of the simple greedy algorithm which has an approximation factor of 2. It works on the basic idea of choosing the city which is farthest from the current set of centers. 

 Step 1: Pick an arbitrary center,c1.
 Step 2: For every remaining cities C1,C2,.. CN-1, compute minimum distnace from the centers chosen already.
 Step 3: Pick the new center with the highest distance from already chosen centers, that is, max((dist(c1,C1),dist(c1,C2),... dist(c1,CN-1)).
 Step 4: Continue this till all the k centers are found.



#### Working ####

For the sample input below:

```
4
0 10 7 6
10 0 8 5
7 8 0 12
6 5 12 0
3
```


 



