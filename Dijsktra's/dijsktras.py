import networkx as nx
import matplotlib.pyplot as plt
import sys
 


def minDistance(dist,sptSet,V):
	print dist
   	min = sys.maxsize

   	for v in range(V):
   		if sptSet[v] == False and dist[v] <= min:
   			min = dist[v]
   			min_index = v
	return min_index


def dijkstra(G,source,pos):

	V=len(G.nodes())
	dist=[]
	parent=[None]*V
	sptSet=[] # sptSet[i] will true if vertex i is included in shortest
               # path tree or shortest distance from src to i is finalized

	for i in range(V):
		dist.append(sys.maxsize)
		sptSet.append(False)

	dist[source] = 0
	parent[source]=-1

	for count in range(V-1):
		u = minDistance(dist, sptSet,V)
		sptSet[u] = True
		for v in range(V):
			print sptSet[u]
			if (u,v) in G.edges():
				if sptSet[v]==False and dist[u] != sys.maxsize and dist[u]+G[u][v]['length'] < dist[v]:
					dist[v] = dist[u] + G[u][v]['length']
					parent[v] = u
	for X in range(V):
		if parent[X]!=-1:
			if (parent[X],X) in G.edges():
				nx.draw_networkx_edges(G,pos,edgelist=[(parent[X],X)],width=2.5,alpha=0.6,edge_color='r')
	return



#takes input from the file and creates a weighted graph
def CreateGraph(G):
	f=open('input.txt')
	n=int(f.readline())
	wtMatrix=[]
	for i in range(n):
		list1=map(int,(f.readline()).split())
		wtMatrix.append(list1)
	source=int(f.readline()) #source vertex for dijsktra's algo 
	#Adds egdes along with their weights to the graph 
	for i in range(n) :
		for j in range(n) :
			if wtMatrix[i][j]>0 :
					G.add_edge(i,j,length=wtMatrix[i][j]) 
	return G,source




#draws the graph and displays the weights on the edges
def DrawGraph(G):
	pos = nx.spring_layout(G)
	nx.draw(G,pos,with_labels=True)  #with_labels=true is to show the node number in the output graph
	edge_labels=dict([((u,v,),d['length'])
             for u,v,d in G.edges(data=True)])
	nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=11) #prints weight on all the edges
	return pos


#main function
if __name__== "__main__":
	G = nx.DiGraph()
	G,source=CreateGraph(G)
	pos=DrawGraph(G)
	dijkstra(G,source,pos)
	plt.show()

