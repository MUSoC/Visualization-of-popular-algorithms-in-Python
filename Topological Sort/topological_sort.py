import networkx as nx
import matplotlib.pyplot as plt
 

#takes input from the file and creates a directed graph
def CreateGraph():
	G = nx.DiGraph()
	f = open('input.txt')
	n = int(f.readline())
	for i in range(n):
		adj_list = map(int, (f.readline()).split()) 
		G.add_edge(adj_list[0], adj_list[1]) 
	return G



#draws the graph
def DrawGraph(G):
	pos = nx.spring_layout(G)
	nx.draw(G, pos, with_labels = True, node_color ='blue')  #with_labels=true is to show the node number in the output graph
	return pos



#main function
if __name__== "__main__":
	G = CreateGraph()
	pos = DrawGraph(G)
	plt.show()

