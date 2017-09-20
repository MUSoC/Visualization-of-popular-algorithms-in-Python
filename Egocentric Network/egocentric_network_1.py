import networkx as nx
import matplotlib.pyplot as plt
 

def EgocentricNetwork(G,v):
	egocentric_network_edge_list = []
	egocentric_network_node_list = [v]
	for i in G.neighbors(v):
		egocentric_network_node_list.append(i)
		egocentric_network_edge_list.append((v,i))
	return egocentric_network_edge_list,egocentric_network_node_list



#takes input from the file and creates a graph
def CreateGraph():
	G = nx.Graph()
	f = open('input.txt')
	n = int(f.readline())
	for i in range(n):
		G.add_node(i+1)
	no_of_edges = int(f.readline())
	for i in range(no_of_edges):
		graph_edge_list = f.readline().split()
		G.add_edge(int(graph_edge_list[0]), int(graph_edge_list[1])) 
	vert = int(f.readline())
	return G, vert



#draws the graph and displays the weights on the edges
def DrawGraph(G,egocentric_network_edge_list,egocentric_network_node_list):
	pos = nx.spring_layout(G)
	nx.draw(G, pos, with_labels = True, node_color = 'blue', alpha = 0.2)  #with_labels=true is to show the node number in the output graph
	nx.draw_networkx_edges(G, pos, edgelist = egocentric_network_edge_list , width = 2.5, alpha = 0.8, edge_color = 'blue')
	nx.draw_networkx_nodes(G,pos, nodelist = egocentric_network_node_list, node_color = 'blue', alpha = 0.5)
	return pos



#main function
if __name__== "__main__":
	G,vert = CreateGraph()
	egocentric_network_edge_list,egocentric_network_node_list = EgocentricNetwork(G,vert)
	DrawGraph(G,egocentric_network_edge_list,egocentric_network_node_list)
	plt.show()

