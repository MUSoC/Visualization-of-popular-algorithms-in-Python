# Visualisation of BFS traversal using networkx library

### INPUT ###


Input is taken from the file 
#### input.txt ####

Sample input
```
4
0 5 10 5
0 0 5 0
0 10 0 0
0 0 10 0
0


```
First line contains the number of nodes,say n.(Nodes are numbered as 0,1,2,...(n-1) )
Followed by n*n weighted matrix. Disconnected egdes are represented by negative weight.
Last line contains the source node.(i.e, the node from which the BFS should begin)


### Draw Graph ###


Graph is first drawn from the weighted matrix input from the user with weights shown. Edges are marked with black.
visualization of the input graph-
![1](https://user-images.githubusercontent.com/22571531/27984139-48d91928-63eb-11e7-9634-fed45cec799a.png)


### BFS traversal ###

Iterative BFS is performed, using a queue. Each time an edge is encountered, 
it is marked with red on the graph through the line -
```
nx.draw_networkx_edges(G,pos,edgelist=[(curr_node,i)],width=2.5,alpha=0.6,edge_color='r')

```
Visualization of the result-
![2](https://user-images.githubusercontent.com/22571531/27984141-4d665e42-63eb-11e7-97e6-49f28ff1552e.png)

### Complexity ###

Time: 0(m+n)                                                                                                        
where m - number of edges                                                                                
n - number of nodes 


