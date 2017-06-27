import networkx as nx
import matplotlib.pyplot as plt
import sys
 


#utility function that returns the minimum distance node
def minDistance(dist, sptSet, V):
   	min = sys.maxsize #assigning largest numeric value to min
   	for v in range(V):
   		if sptSet[v] == False and dist[v] <= min:
   			min = dist[v]
   			min_index = v
	return min_index



#function that performs dijsktras algorithm on the graph G,with source vertex as source
def dijsktras(G, source, pos):
	V = len(G.nodes()) # V denotes the number of vertices in G
	dist = [] # dist[i] will hold the shortest distance from source to i
	parent = [None]*V # parent[i] will hold the node from which i is reached to, in the shortest path from source
	sptSet = [] # sptSet[i] will hold true if vertex i is included in shortest path tree
	#initially, for every node, dist[] is set to maximum value and sptSet[] is set to False
	for i in range(V):
		dist.append(sys.maxsize)
		sptSet.append(False)
	dist[source] = 0
	parent[source]= -1 #source is itself the root, and hence has no parent
	for count in range(V-1):
		u = minDistance(dist, sptSet, V) #pick the minimum distance vectex from the set of vertices
		sptSet[u] = True
		#update the vertices adjacent to the picked vertex
		for v in range(V):
			if (u, v) in G.edges():
				if sptSet[v] == False and dist[u] != sys.maxsize and dist[u] + G[u][v]['length'] < dist[v]:
					dist[v] = dist[u] + G[u][v]['length']
					parent[v] = u
	#marking the shortest path from source to each of the vertex with red, using parent[]
	for X in range(V):
		if parent[X] != -1: #ignore the parent of root node 
			if (parent[X], X) in G.edges():
				nx.draw_networkx_edges(G, pos, edgelist = [(parent[X], X)], width = 2.5, alpha = 0.6, edge_color = 'r')
	return



#takes input from the file and creates a weighted graph
def CreateGraph():
	G = nx.DiGraph()
	f = open('input.txt')
	n = int(f.readline())
	wtMatrix = []
	for i in range(n):
		list1 = map(int, (f.readline()).split())
		wtMatrix.append(list1)
	source = int(f.readline()) #source vertex for dijsktra's algo 
	#Adds egdes along with their weights to the graph 
	for i in range(n) :
		for j in range(n) :
			if wtMatrix[i][j] > 0 :
					G.add_edge(i, j, length = wtMatrix[i][j]) 
	return G, source



#draws the graph and displays the weights on the edges
def DrawGraph(G):
	pos = nx.spring_layout(G)
	nx.draw(G, pos, with_labels = True)  #with_labels=true is to show the node number in the output graph
	edge_labels = dict([((u, v), d['length']) for u, v, d in G.edges(data = True)])
	nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, label_pos = 0.3, font_size = 11) #prints weight on all the edges
	return pos



#main function
if __name__ == "__main__":
	G,source = CreateGraph()
	pos = DrawGraph(G)
	dijsktras(G, source, pos)
	plt.show()

