import networkx as nx
import numpy as np
import random
from operator import itemgetter
def page_rank(G):
	m = G.number_of_nodes()
	itr = 1000000
	count = {}
	for i in range(0,m):
		count[str(i)] = i
	#print(count)
	for i in range(0,itr):
		r = random.randint(0,m-1)
		#print(r)
		succ = G.successors(r)
		r1 = random.randint(0,itr)
		if r1 < int(0.2*itr):
			r = random.randint(0,m-1)
		for s in succ:
				count[str(s)] = count[str(s)] + 1
	#print(count1)
	#print(count)
	count1 = sorted(count.items(), key = itemgetter(1), reverse = True)
	#print(count1)
	pagerank1 = []
	for k in count1:
		pagerank1.append(int(k[0]))

	return pagerank1

def isEdge(G,i,j):
	succ = G.successors(i)
	if i == j:
		return 0
	if j in succ:
		return 1
	return 0


def updated_pagerank(G,initial_guess,d):
	m = G.number_of_nodes()
	itr = 10000
	count = np.zeros(m,dtype = int)
	Pr = initial_guess.copy()
	for i in range(0,m):
		succ = G.successors(i)
		count[i] = len(list(succ))
	#print(count)
	#print(sum(count))
	for i in range(0,itr):
		#print(Pr)
		for j in range(0,m):
			_sum = 0
			for k in range(0,m):
				#print(i,isEdge(G,k,j))
				if count[k] != 0:
					_sum = _sum + ((d*isEdge(G,k,j)*initial_guess[k])/count[k])
			Pr[j] = _sum + (1-d)
		initial_guess = Pr.copy()
	Pr_final = np.zeros(m,dtype = int) 
	print(Pr)
	for i in range(0,m):
		p = np.argmax(Pr)
		Pr[p] = -1
		Pr_final[i] = p
	return Pr_final



print("This program will determine the pagerank of Nodes based on their ability of being found interesting")
print(" ")
#print("This is a naive approach in which we start at a random node every time and see its neighbors. We maintain a count of the number of times a particular node has been pointed towards. We repeat this experiment at least 1000000 times to get a good approximation of the pagerank.")
G = nx.DiGraph()
e = open("pagerank.txt", "r")
lines = e.read().splitlines()
#print(len(lines))
line_set = set()
line_set.add(line for line in lines)
#print(len(list(line_set)))
nodes = set()
for line in lines:
	#print(line)
	node1 = line.split(' ')
	nodes.add(int(node1[0]))
	nodes.add(int(node1[1]))
nodes1 = list(nodes)
no_of_nodes = len(nodes1)
nodes1.sort()
#print(nodes1)
prev_to_curr = {}
curr_to_prev = {}
for i in range(0,no_of_nodes):
	prev_to_curr[nodes1[i]] = i
	curr_to_prev[i] = nodes1[i]
G.add_nodes_from(i for i in range(0,no_of_nodes))
for line in lines:
	a = line.split(' ')
	G.add_edge(prev_to_curr[int(a[0])],prev_to_curr[int(a[1])])

#print(list(G.nodes()))
#print(G.edges())
'''for i in range(0,500):
	r1 = random.randint(0,99)
	r2 = random.randint(0,99)
	if r1!=r2:
		G.add_edge(r1,r2)
'''
print("The number of nodes in the directed graph is ", G.number_of_nodes())
#print(G.edges)
print("The number of edges in the directed graph is ", G.number_of_edges())
pr = page_rank(G)
initial_guess = np.ones(G.number_of_nodes(),dtype= float)
d = 0.85
initial_guess[:] = 0.01
pr1 = updated_pagerank(G,initial_guess,d)
#print("The list of nodes sorted in ascending order according to their pagerank is:")
print("Previous pagerank was: ")
print(pr)
for i in range(0,len(pr)):
	pr[i] = curr_to_prev[pr[i]]
print("Updated pagerank is : ")
print(pr1)
#for i in range(0,len(pr1)):
#	pr1[i] = curr_to_prev[pr1[i]]
print("Built in pagerank is ")
builtin = nx.pagerank(G,alpha = 0.85, max_iter = 100)
builtin1 = sorted(builtin.items(), key = itemgetter(1), reverse = True)
b = []
for k in builtin1:
		b.append(int(k[0])) 
print(b)
error = 0
m = len(pr)
updated_idx = np.zeros(m,dtype = int)
builtin_idx = np.zeros(m,dtype = int)
for i in range(0,m):
	builtin_idx[builtin1[i][0]] = i
	updated_idx[pr1[i]] = i
print("Index matrices are")
print(updated_idx)
print(builtin_idx)
for i in range(0,m):
	error = error + abs(updated_idx[i]- builtin_idx[i])
print("Error is", error/m)
