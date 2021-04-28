#Breadth First Search

#Class Vertex
class Vertex:
	def __init__(self, n):
		self.name = n
		#initialize a list of neighbors
		self.neighbors = list()
		
		#Initilize the distance at a high value and the color an unvisited vertice
		self.distance = 9999
		self.color = 'black'
	
	#Add neighbors to the list and sort the list
	def add_neighbor(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()

#Graph class
class Graph:
    #Initalize a dictionary
	vertices = {}
	
	#Check to makes sure that the vertex passed is a vertex object and that its not in vertices, add to dictionary
	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False
	
	#Adds an edge
	def add_edge(self, u, v):
		if u in self.vertices and v in self.vertices:
			for key, value in self.vertices.items():
				
				#Find vertex for the neighbor
				if key == u:
					value.add_neighbor(v)
				if key == v:
					value.add_neighbor(u)
			return True
		else:
			return False
	
	#iterate though the vertices to print the graph
	def print_graph(self):
		for key in sorted(list(self.vertices.keys())):
			print(key + str(self.vertices[key].neighbors) + "  " + str(self.vertices[key].distance))
	
	#Take a vertex object as a starting point. Creates a queue to process the vertices
	def bfs(self, vert):
		q = list()
		vert.distance = 0
		vert.color = 'red'
		#Determines the distance of the neighbors, append neighbors to the queue
		for v in vert.neighbors:
			self.vertices[v].distance = vert.distance + 1
			q.append(v)
		
		#FIFO off the queue
		while len(q) > 0:
			u = q.pop(0)
			node_u = self.vertices[u]
			node_u.color = 'red'
			
			#In neighbors, get the vertex object of each neighbor, if neighbor has not be visited, append to the vertex
			for v in node_u.neighbors:
				node_v = self.vertices[v]
				if node_v.color == 'black':
					q.append(v)
					#Update distance
					if node_v.distance > node_u.distance + 1:
						node_v.distance = node_u.distance + 1
#Assign a graph object					
g = Graph()
#Assign a Vertex to the graph
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
	g.add_vertex(Vertex(chr(i)))
#Assign edges
edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
	g.add_edge(edge[:1], edge[1:])
	
g.bfs(a)
g.print_graph()