import networkx as nx
import matplotlib.pyplot as plt
import sys


#takes input from the file and creates a weighted graph
def CreateGraph():
	G = nx.Graph()
	f = open('input.txt')
	n = int(f.readline())
	wtMatrix = []
	for i in range(n):
		list1 = map(int, (f.readline()).split())
		wtMatrix.append(list1)
	#Adds egdes along with their weights to the graph 
	for i in range(n) :
		for j in range(n)[i:] :
				G.add_edge(i, j, length = wtMatrix[i][j]) 
	return G



#draws the graph and displays the weights on the edges
def DrawGraph(G):
	pos = nx.spring_layout(G)
	nx.draw(G, pos, with_labels = True)  #with_labels=true is to show the node number in the output graph
	edge_labels = nx.get_edge_attributes(G,'length')
	nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, font_size = 11) #prints weight on all the edges
	return pos



#main function
if __name__ == "__main__":
	G = CreateGraph()
	pos = DrawGraph(G)
	#prims(G, pos)
	plt.show()

