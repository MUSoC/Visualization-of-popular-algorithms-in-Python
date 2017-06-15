# Visualisation of DFS traversal using networkx library

### INPUT ###

Graph is first drawn from the weighted matrix input from the user. 
Input is taken from the file 
#### input.txt ####

Sample input
```
 4
 0 5 0 5
 5 0 5 0
 0 5 0 5
 5 0 5 0
 0

```
First line contains the number of nodes,say n.(Nodes are numbered as 0,1,2,...(n-1) )
Followed by n*n weighted matrix. Disconnected egdes are represented by negative weight.
Last line contains the source node.(i.e, the node from which the DFS should begin)



### DFS traversal ###

Recursive DFS is performed, resulting DFS forests are stored in a stack. 



### Visulization of DFS path ###

The stack is then used to mark the DFS traversed edges with a different colour(So, as to distinguish itself from the rest).