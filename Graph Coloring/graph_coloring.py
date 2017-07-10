import networkx as nx
import matplotlib.pyplot as plt


#implementation of welsh_powell algorithm
def welsh_powell(G):
	#sorting the nodes based on it's valency
	node_list = sorted(G.nodes(), key =lambda x:G.neighbors(x))
	col_val = {} #dictionary to store the colors assigned to each node
	col_val[node_list[0]] = 0 #assign the first color to the first node
	# Assign colors to remaining N-1 nodes
	for node in node_list[1:]:
		available = [True] * len(G.nodes()) #boolean list[i] contains false if the node color 'i' is not available

		#iterates through all the adjacent nodes and marks it's color as unavailable, if it's color has been set already
		for adj_node in G.neighbors(node): 
			if adj_node in col_val.keys():
				col = col_val[adj_node]
				available[col] = False
		clr = 0
		for clr in range(len(available)):
			if available[clr] == True:
				break
		col_val[node] = clr
	print col_val
	return col_val

        



#takes input from the file and creates a undirected graph
def CreateGraph():
	G = nx.Graph()
	f = open('input.txt')
	n = int(f.readline())
	for i in range(n):
		graph_edge_list = f.readline().split()
		G.add_edge(graph_edge_list[0], graph_edge_list[1]) 
	return G


#draws the graph and displays the weights on the edges
def DrawGraph(G,col_val):
	pos = nx.spring_layout(G)
	values = [col_val.get(node, 'blue') for node in G.nodes()]
	nx.draw(G, pos, with_labels = True, node_color = values, edge_color = 'black' ,width = 1, alpha = 0.7)  #with_labels=true is to show the node number in the output graph




#main function
if __name__ == "__main__":
	G = CreateGraph()
	col_val = welsh_powell(G)
	DrawGraph(G,col_val)
	plt.show()