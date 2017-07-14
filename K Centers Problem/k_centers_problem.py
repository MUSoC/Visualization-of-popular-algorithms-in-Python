import networkx as nx
import matplotlib.pyplot as plt
import sys
import operator



def k_centers(G,n):
	centres = []
	cities = G.nodes()
	#add an arbitrary node, here, the first node,to he centers list
	centres.append((G.nodes())[0])
	cities.remove(centres[0]) 
	n = n-1 #since we have already added one center
	while n!=0:
		city_dict = {}
		for cty in cities:
			min_dist=float("inf")
			for c in centres:
				min_dist=min(min_dist,G[cty][c]['length'])
			city_dict[cty]=min_dist
		print city_dict
		new_center = max(city_dict, key=lambda i: city_dict[i])
		print new_center
		centres.append(new_center)
		cities.remove(new_center)
		n = n-1
		#new_center,_ = max(city_dict.iteritems(), key = lambda x:city_dict[x])
		#centres.append(new_center)
		#cities.remove(new_center)
	print centres


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
	n = 2
	k_centers(G, n)
	plt.show()

