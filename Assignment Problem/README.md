# Visualisation of Assignment Problem using networkx library

### INPUT ###


Input is taken from the file 
#### input.txt ####

Sample input
```
 4
 9 2 7 8
 6 4 3 7 
 5 8 1 8
 7 6 9 4

```
First line contains n, the number of people which is the same as the number of jobs.
Followed by n*n weighted profit matrix.


### Draw Graph ###


A bipartite graph is to be drawn. Person and Job - are the 2 sets of nodes. Since, person is connected to every possible job and a job has connection from every person.

![1](https://user-images.githubusercontent.com/22571531/27514223-5fa03ec4-59a1-11e7-9bdc-8d9c17afc030.png)


### Assignment Problem ###

Assignment Problem is a combinatorial optimization problem. It consists of finding a maximum weight matching (or minimum weight perfect matching) in a weighted bipartite graph.

Here, we have n people and n jobs that need to be done. Given profit matrix, we need to assign exactly one person to each job and exactly one job to each person in such a way that the total profit of the assignment in maximized.
(It is a linear assignment problem, since number of people and jobs are equal.)

Hungarian algorithm is one of the most effient methods that solves the linear assignment problem in polynomial time(with a time complexity of O(n^3)).

The code here,is an implementation of Hungarian algorithm. 
The resultant graph for the sample input with maximum weight matching (denoted by red edges):

![2](https://user-images.githubusercontent.com/22571531/27514224-645f8028-59a1-11e7-92b0-5f0d7f0b8b02.png)

#### Complexity ####

Time: O(n^3)                                                          
n - number of people( = number of jobs)
