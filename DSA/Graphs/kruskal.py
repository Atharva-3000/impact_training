#kruskal algo used to find min cost spanning tree.
#1. Arrange all edges in ascending order(lower to higher based on cost)
#2. Consider least cost weighted edge and include in tree, if it forms a cycle just ignore and consider next least cost weighted edge.
#3. repeat step 2 such a way that all vertices are included, finally it should have n vertices and n-1 edges.
# Python program for Kruskal's algorithm to find 
# Minimum Spanning Tree of a given connected, 
# undirected and weighted graph 

class Graph: 
	def __init__(self, vertices): 
		self.V = vertices 
		self.graph = [] 

	def addEdge(self, u, v, w): 
		self.graph.append([u, v, w]) 
		
	def find(self, parent, i): 
		if parent[i] != i: 
			parent[i] = self.find(parent, parent[i]) 
		return parent[i] 

	def union(self, parent, rank, x, y): 
		if rank[x] < rank[y]: 
			parent[x] = y 
		elif rank[x] > rank[y]: 
			parent[y] = x 
		else: 
			parent[y] = x 
			rank[x] += 1
	def KruskalMST(self): 
		result = [] 
		i = 0
		e = 0
		self.graph = sorted(self.graph, key=lambda item: item[2]) 
		parent = [] 
		rank = [] 
		for node in range(self.V): 
			parent.append(node) 
			rank.append(0) 
		while e < self.V - 1: 
			u, v, w = self.graph[i] 
			i = i + 1
			x = self.find(parent, u) 
			y = self.find(parent, v) 
			if x != y: 
				e = e + 1
				result.append([u, v, w]) 
				self.union(parent, rank, x, y)
		minimumCost = 0
		print("Edges in the constructed MST") 
		for u, v, weight in result: 
			minimumCost += weight 
			print("%d -- %d == %d" % (u, v, weight)) 
		print("Minimum Spanning Tree", minimumCost) 

if __name__ == '__main__': 
	g = Graph(6) 
	g.addEdge(0, 1, 2) 
	g.addEdge(0, 2, 3) 
	g.addEdge(1, 2, 5) 
	g.addEdge(1, 3, 3) 
	g.addEdge(1, 4, 4) 
	g.addEdge(2, 4, 4) 
	g.addEdge(3, 4, 2) 
	g.addEdge(3, 5, 3) 
	g.addEdge(4, 5, 5) 
	g.KruskalMST()