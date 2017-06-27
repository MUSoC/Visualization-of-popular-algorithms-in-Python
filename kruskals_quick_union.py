import networkx as nx
import matplotlib.pyplot as plt
import sys



# A utility function that return the smallest unprocessed edge
def getMin(G, mstFlag):
    min = sys.maxsize  # assigning largest numeric value to min
    for i in [(u, v, edata['length']) for u, v, edata in G.edges( data = True) if 'length' in edata ]:
    	if mstFlag[i] == False and i[2] < min:
    		min = i[2]
    		min_edge = i
    return min_edge

	

# A utility function to find root or origin of the node i in MST
def findRoot(parent, i):
    if parent[i] == i:
        return i
    return findRoot(parent, parent[i])



# A function that does union of set x and y based on the order
def union(parent, order, x, y):
    xRoot = findRoot(parent, x)
    yRoot = findRoot(parent, y)
 	# Attach smaller order tree under root of high order tree
    if order[xRoot] < order[yRoot]:
        parent[xRoot] = yRoot
    elif order[xRoot] > order[yRoot]:
        parent[yRoot] = xRoot
    # If orders are same, then make any one as root and increment its order by one
    else :
        parent[yRoot] = xRoot
        order[xRoot] += 1



# function that performs Kruskals algorithm on the graph G
def kruskals(G, pos):
	eLen = len(G.edges()) # eLen denotes the number of edges in G
	vLen = len(G.nodes()) # vLen denotes the number of vertices in G
	mst = [] # mst contains the MST edges
	mstFlag = {} # mstFlag[i] will hold true if the edge i has been processed for MST
	for i in [ (u, v, edata['length']) for u, v, edata in G.edges(data = True) if 'length' in edata ]:
		mstFlag[i] = False 

	parent = [None] * vLen # parent[i] will hold the vertex connected to i, in the MST
	order = [None] * vLen	# order[i] will hold the order of appearance of the node in the MST
	for v in range(vLen):
		parent[v] = v
		order[v] = 0
	while len(mst) < vLen - 1 :
		curr_edge = getMin(G, mstFlag) # pick the smallest egde from the set of edges
		mstFlag[curr_edge] = True # update the flag for the current edge
		y = findRoot(parent, curr_edge[1])
		x = findRoot(parent, curr_edge[0])
		# adds the edge to MST, if including it doesn't form a cycle
		if x != y:
			mst.append(curr_edge)
			union(parent, order, x, y)
        # Else discard the edge
    # marks the MST edges with red
	for X in mst:
	 	if (X[0], X[1]) in G.edges():
	 		nx.draw_networkx_edges(G, pos, edgelist = [(X[0], X[1])], width = 2.5, alpha = 0.6, edge_color = 'r')
	return



# takes input from the file and creates a weighted graph
def CreateGraph():
	G = nx.Graph()
	f = open('input.txt')
	n = int(f.readline())
	wtMatrix = []
	for i in range(n):
		list1 = map(int, (f.readline()).split())
		wtMatrix.append(list1)
	# Adds egdes along with their weights to the graph 
	for i in range(n) :
		for j in range(n)[i:] :
			if wtMatrix[i][j] > 0 :
					G.add_edge(i, j, length = wtMatrix[i][j]) 
	return G



# draws the graph and displays the weights on the edges
def DrawGraph(G):
	pos = nx.spring_layout(G)
	nx.draw(G, pos, with_labels = True)  # with_labels=true is to show the node number in the output graph
	edge_labels = nx.get_edge_attributes(G, 'length')
	nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, font_size = 11) #    prints weight on all the edges
	return pos



# main function
if __name__ == "__main__":
	G = CreateGraph()
	pos = DrawGraph(G)
	kruskals(G, pos)
	plt.show()

