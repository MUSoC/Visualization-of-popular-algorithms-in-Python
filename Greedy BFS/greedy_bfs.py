import networkx as nx
import matplotlib.pyplot as plt
import Queue as Q
 
 

def getPriorityQueue(list):
	q = Q.PriorityQueue()
	for node in list:
		q.put(Ordered_Node(heuristics[node],node))
	return q,len(list)



def greedyBFSUtil(G, v, visited, q, dest, flag): 
	if flag == 1:
		return flag
	visited[v] = True
	q.put(Ordered_Node(heuristics[v], v))
	if v == dest:
		flag = 1
	else:
		list1 = []
		pq,size = getPriorityQueue(G[v])
		for i in range(size):
			list1.append(pq.get().description)
		for i in list1:
			if flag != 1:
				#print "current city:", i
				if visited[i] == False :
					flag = greedyBFSUtil(G, i, visited, q, dest, flag)
	return flag


 
def greedyBFS(G, source, dest, heuristics, pos): 
	visited = {}
	for node in G.nodes():
		visited[node] = False
 	q = Q.PriorityQueue()
	flag = greedyBFSUtil(G, source, visited, q, dest, 0)
	prev = -1
	path = list(q.queue)
	for var in path:
		if prev != -1:
			curr = var.description
			nx.draw_networkx_edges(G, pos, edgelist = [(prev,curr)], width = 2.5, alpha = 0.6, edge_color = 'black')
			prev = curr
		else:
			prev = var.description
	return



class Ordered_Node(object):
	def __init__(self, priority, description):
		self.priority = priority
		self.description = description
		return
	def __cmp__(self, other):
		return cmp(self.priority, other.priority)

def getHeuristics(G):
	heuristics = {}
	f = open('heuristics.txt')
	for i in G.nodes():
		list1 = f.readline().split()
		heuristics[list1[0]] = list1[1]
	return heuristics



#takes input from the file and creates a weighted graph
def CreateGraph():
	G = nx.Graph()
	f = open('input.txt')
	n = int(f.readline())
	for i in range(n):
		list1 = f.readline().split()
		G.add_edge(list1[0], list1[1], length = list1[2]) 
	source, dest= f.read().splitlines()
	return G, source, dest



def DrawPath(G, source, dest):
	pos = nx.spring_layout(G)
	val_map = {}
	val_map[source] = 'green'
	val_map[dest] = 'red'
	values = [val_map.get(node, 'blue') for node in G.nodes()]
	nx.draw(G, pos, with_labels = True, node_color = values, edge_color = 'b' ,width = 1, alpha = 0.5)  #with_labels=true is to show the node number in the output graph
	edge_labels = dict([((u, v,), d['length']) for u, v, d in G.edges(data = True)])
	nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, label_pos = 0.3, font_size = 11) #prints weight on all the edges
	return pos



#main function
if __name__ == "__main__":
	G, source,dest = CreateGraph()
	heuristics = getHeuristics(G)
	pos = DrawPath(G, source, dest)
	greedyBFS(G, source, dest, heuristics, pos)
	plt.show()




