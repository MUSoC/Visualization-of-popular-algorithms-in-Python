import networkx as nx
import matplotlib.pyplot as plt
import itertools
 

def EgocentricNetwork(G,v):
	
	egocentric_network_edge_list = []
	egocentric_network_node_list = [v]
	for i in G.neighbors(v):
		egocentric_network_node_list.append(i)
		egocentric_network_edge_list.append((v,i))
	egocentric_network_node_list.sort()
	egocentric_network_edge_list = list(tuple(sorted(p)) for p in egocentric_network_edge_list)

	for i in list(itertools.combinations(egocentric_network_node_list, 2)): #generates all possible pairs of nodes
		if i in G.edges() and i not in egocentric_network_edge_list:
			egocentric_network_edge_list.append(i)

	
	temp = []
	temp.extend(egocentric_network_node_list)

	for i in temp:#print i," ",G.neighbors(i)
		for j in G.neighbors(i):
			if j not in egocentric_network_node_list:
				egocentric_network_node_list.append(j)
			if (j,i) in G.edges() and (j,i) not in egocentric_network_edge_list:
				egocentric_network_edge_list.append((j,i))
			elif (i,j) in G.edges() and (i,j) not in egocentric_network_edge_list:
				egocentric_network_edge_list.append((i,j))
	print egocentric_network_edge_list
	print egocentric_network_node_list
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


def DrawGraph(G, egocentric_network_edge_list, egocentric_network_node_list, vert):
	pos = nx.spring_layout(G)
	nx.draw(G, pos, with_labels = True, node_color = 'blue', alpha = 0.8)  #with_labels=true is to show the node number in the output graph
	nx.draw_networkx_edges(G, pos, edgelist = egocentric_network_edge_list , width = 2.5, alpha = 0.8, edge_color = 'red')
	nx.draw_networkx_nodes(G,pos, nodelist = egocentric_network_node_list, node_color = 'red', alpha = 0.5)
	nx.draw_networkx_nodes(G,pos,nodelist=[vert],node_color='green',node_size=500,alpha=0.8)
	return pos


def CentralityMeasures(G):
	# Betweenness centrality
	bet_cen = nx.betweenness_centrality(G)
	# Closeness centrality
	clo_cen = nx.closeness_centrality(G)
	# Eigenvector centrality
	eig_cen = nx.eigenvector_centrality(G)
	# Degree centrality
	deg_cen = nx.degree_centrality(G)
	#print bet_cen, clo_cen, eig_cen
	print "# Betweenness centrality:" + str(bet_cen)
	print "# Closeness centrality:" + str(clo_cen)
	print "# Eigenvector centrality:" + str(eig_cen)
	print "# Degree centrality:" + str(deg_cen)


#main function
if __name__== "__main__":
	G,vert = CreateGraph()
	egocentric_network_edge_list,egocentric_network_node_list = EgocentricNetwork(G,vert)
	DrawGraph(G,egocentric_network_edge_list,egocentric_network_node_list, vert)
	CentralityMeasures(G)
	plt.show()

