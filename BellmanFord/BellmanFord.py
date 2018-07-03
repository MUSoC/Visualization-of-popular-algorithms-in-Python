import networkx as nx
import matplotlib.pyplot as plt
import sys

inf = float('inf')

#function that performs Bellman-Ford algorithm on the graph G,with source vertex as source
def bellmanFord(G, source, pos):
	V = len(G.nodes()) # V denotes the number of vertices in G
	dist = [] # dist[i] will hold the shortest distance from source to i
	parent = [None]*V # parent[i] will hold the node from which i is reached to, in the shortest path from source

	for i in range(V):
		dist.append(inf)

	parent[source] = -1; #source is itself the root, and hence has no parent
	dist[source] = 0;

	for i in range(V-1):
		for u, v, d in G.edges(data = True): # Relaxation is the most important step in Bellman-Ford. It is what increases the accuracy of the distance to any given vertex. Relaxation works by continuously shortening the calculated distance between vertices comparing that distance with other known distances.
			if dist[u] + d['length'] < dist[v]: #Relaxation Equation
				dist[v] = d['length'] + dist[u]
				parent[v] = u

	#marking the shortest path from source to each of the vertex with red, using parent[]
	for v in range(V):
		if parent[v] != -1: #ignore the parent of root node
			if (parent[v], v) in G.edges():
				nx.draw_networkx_edges(G, pos, edgelist = [(parent[v], v)], width = 2.5, alpha = 0.6, edge_color = 'r')
	return

#takes input from the file and creates a weighted graph
def createGraph():
	G = nx.DiGraph()
	f = open('input.txt')
	n = int(f.readline())
	wtMatrix = []
	for i in range(n):
		list1 = map(int, (f.readline()).split())
		wtMatrix.append(list1)
	source = int(f.readline()) #source vertex for BellmanFord algo
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
	G, source = createGraph()
	pos = DrawGraph(G)
	bellmanFord(G, source, pos)
	plt.show()
