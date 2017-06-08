import networkx as nx
import matplotlib.pyplot as plt
 

#utility fucntion used by DFS which does recursive depth first search 
def DFSUtil(G, v, visited,sl): 
	visited[v]= True
	sl.append(v) 
	for i in G[v]:
		if visited[i] == False:
			DFSUtil(G, i, visited,sl)
	return sl
 

#DFS traversal 
def DFS(G,source): 
	visited =[False]*(len(G.nodes()))
 	sl=[]		#a list that stores dfs forest starting with source node
 	dfs_stk=[] #A nested list that stores all the DFS Forest's
	dfs_stk.append(DFSUtil(G,source, visited,sl))
	for i in range(len(G.nodes())):
		if visited[i] == False:
			sl=[]
			dfs_stk.append(DFSUtil(G, i, visited,sl))
	return dfs_stk

			


#takes input from the file and creates a weighted graph
def CreateGraph(G):
	f=open('input.txt')
	n=int(f.readline())
	wtMatrix=[]
	for i in range(n):
		list1=map(int,(f.readline()).split())
		wtMatrix.append(list1)
	source=int(f.readline()) #source vertex from where DFS has to start
	#Graph creation
	G = nx.Graph()
	#Adds weight to the edges 
	for i in range(n) :
		for j in range(n) :
			if wtMatrix[i][j]>0 :
				G.add_edge(i,j,weight=wtMatrix[i][j]) 
	return G,source




#marks all edges traversed through DFS with red
def DrawDFSPath(G,dfs_stk):
	pos = nx.spring_layout(G)
	nx.draw(G,pos)
	labels = nx.get_edge_attributes(G,'weight')
	nx.draw_networkx_edge_labels(G,pos,edge_labels=labels,edge_color='r',alpha=0.5 )    #prints weight on all the edges


	for i in dfs_stk:
		if(len(i)>1):
			for j in i[:(len(i)-1)]:
				if i[i.index(j)+1] in G[j]:
					nx.draw_networkx_edges(G,pos,edgelist=[(j,i[i.index(j)+1])],width=8,alpha=0.5,edge_color='r')
				else:
					for k in i[1::-1]: #if in case the path was reversed coz all the possible neighbours were visited, we need to find the adj node to it.
						if k in G[j]:
							nx.draw_networkx_edges(G,pos,edgelist=[(j,k)],width=8,alpha=0.5,edge_color='r')
							break
	plt.show()


#main function
if __name__== "__main__":
	G = nx.Graph()
	G,source=CreateGraph(G)
	dfs_stk=DFS(G,source)
	DrawDFSPath(G,dfs_stk)