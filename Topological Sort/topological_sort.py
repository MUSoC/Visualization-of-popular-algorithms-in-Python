import networkx as nx
import matplotlib.pyplot as plt
 

def topologicalSort(G,pos):
	zero_indeg_list = [] 
	sorted_list = []
	visited = [False]*len(G.nodes())
	while len(G.nodes())!=0:
		for node in G.nodes():
			if visited[node-1] == False:
				if G.in_degree(node) == 0:
					visited[node-1] = True
					zero_indeg_list.append(node)
		for node in zero_indeg_list:
			sorted_list.append(node)
			G.remove_node(node)
			zero_indeg_list.remove(node)
	return sorted_list

		
#takes input from the file and creates a directed graph
def CreateResultGraph(sorted_list):
	D = nx.DiGraph()
	for i in range(len(sorted_list)-1): 
	 	D.add_edge(sorted_list[i], sorted_list[i+1]) 
	pos = nx.spring_layout(D)
	val_map = {}
	val_map[sorted_list[0]] = 'green'
	val_map[sorted_list[len(sorted_list)-1]] = 'red'
	values = [val_map.get(node, 'blue') for node in D.nodes()]
	nx.draw(D, pos, with_labels = True, node_color =values)
	

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
	plt.figure(1)
	pos = DrawGraph(G)
	plt.figure(2)
	sorted_list = topologicalSort(G,pos)
	CreateResultGraph(sorted_list)
	plt.show()

