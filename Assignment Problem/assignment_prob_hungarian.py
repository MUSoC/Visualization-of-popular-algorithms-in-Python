import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite
from string import ascii_lowercase



def init_labels(cost):
	n = len(cost)
	lx = [0] * n
	ly = [0] * n
 	for x in range(n):
 		for y in range(n):
 			lx[x] = max(lx[x], cost[x][y])
 	return lx,ly



def update_labels(T, slack, S, lx, ly, n):
	delta = float("inf");
	for y in range(n):
		if T[y] == 0:
			delta = min(delta, slack[y])
 	for x in range(n):
		if S[x] != 0:
			lx[x] -= delta
 	for y in range(n):
		if T[y] != 0:
			ly[y] += delta
 	for y in range(n):
 		if T[y] == 0:
			slack[y] -= delta



def add_to_tree(x, prevx, S, prev, lx, ly, slack, slackx, cost):
	n = len(cost)
	S[x] = True
 	prev[x] = prevx
 	for y in range(n):
 		if (lx[x] + ly[y] - cost[x][y]) < slack[y]:
 			slack[y] = lx[x] + ly[y] - cost[x][y]
 			slackx[y] = x
 


def augment(cost, max_match, xy, yx, lx, ly, slack, slackx):
	n = len(cost)
	if max_match == n:
		return;
 	q = [0] * n
	wr = 0
	rd = 0
	root = 0
	S = [False] * n
	T = [False] * n
	prev = [-1] * n 
	for x in range(n):
		if xy[x] == -1:
			q[wr] = x
			wr = wr+1
			root = x
 			prev[x] = -2
 			S[x] = True
 			break
 	for y in range(n): 
 		slack[y] = lx[root] + ly[y] - cost[root][y]
 		slackx[y] = root
  	while True:
 		while rd < wr:
 			x = q[rd]
 			rd = rd+1
 			for y in range(n):
 				if (cost[x][y] == lx[x] + ly[y] and T[y] == 0):
					if yx[y] == -1:
						break
 					T[y] = True
 					q[wr] = yx[y]
 					wr = wr+1
 					add_to_tree(yx[y], x, S, prev, lx, ly, slack, slackx, cost)
 			if y < n:
 				break
		if y < n:
			break
		update_labels(T, slack, S, lx, ly, n)
		wr = 0 
		rd = 0
 		for y in range(n):
			if T[y] == 0 and slack[y] == 0:
				if yx[y] == -1:
					x = slackx[y]
 					break
 				else:
					T[y] = true
 					if S[yx[y]] == 0:
 						q[wr] = yx[y]
 						wr = wr+1
 						add_to_tree(yx[y], slackx[y], S, prev, lx, ly, slack, slackx, cost)
 		if y < n:
			break
	if y < n:
		max_match = max_match+1
		cx = x
		cy = y
		ty = 0
		flag = 0
		if cx != -2:
			ty = xy[cx];
 			yx[cy] = cx;
 			xy[cx] = cy;
 			cx = prev[cx]
			cy = ty
		while cx != -2:
			ty = xy[cx]
 			yx[cy] = cx
			xy[cx] = cy
			cx = prev[cx]
			cy = ty
 		augment(cost, max_match, xy, yx, lx, ly, slack, slackx)



def hungarian(B ,pos ,cost):
	n = len(cost)
	ret = 0; 
	max_match = 0 
	xy = [-1] * n
	yx = [-1] * n
	slack = [0] * n
	slackx = [0] * n
	lx, ly = init_labels(cost)
	augment(cost, max_match, xy, yx, lx, ly, slack, slackx)
	for x in range(n):
 		if (x, chr(xy[x]+97)) in B.edges():
			nx.draw_networkx_edges(B, pos, edgelist = [(x, chr(xy[x]+97))], width = 2.5, alpha = 0.6, edge_color = 'r')



#takes input from the file and creates a weighted bipartite graph
def CreateGraph():
	B = nx.DiGraph();
	f = open('input.txt')
	n = int(f.readline())
	cost = []
	
	for i in range(n):
		list1 = map(int, (f.readline()).split())
		cost.append(list1)
	people = []
	for i in range(n):
		people.append(i)
	job = [] 
	for c in ascii_lowercase[:n]:
		job.append(c)
	B.add_nodes_from(people, bipartite=0) # Add the node attribute "bipartite"
	B.add_nodes_from(job, bipartite=1)
	for i in range(n) :
		for c in ascii_lowercase[:n] :
			if cost[i][ord(c)-97] > 0 :
				B.add_edge(i, c, length = cost[i][ord(c)-97])  
	return B,cost



def DrawGraph(B):
	l, r = nx.bipartite.sets(B)
	pos = {}
	# Update position for node from each group
	pos.update((node, (1, index)) for index, node in enumerate(l))
	pos.update((node, (2, index)) for index, node in enumerate(r))
	nx.draw(B, pos, with_labels = True)  #with_labels=true is to show the node number in the output graph
	edge_labels = dict([((u, v), d['length']) for u, v, d in B.edges(data = True)])
	nx.draw_networkx_edge_labels(B, pos, edge_labels = edge_labels, label_pos = 0.2, font_size = 11) #prints weight on all the edges
	return pos



#main function
if __name__ == "__main__":
	B, cost = CreateGraph();
	pos = DrawGraph(B)
	hungarian(B, pos, cost)
	plt.show()
	