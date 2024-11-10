import heapq

class Node:
	def __init__(self,state,parent=None,g=0,h=0):
		self.state = state
		self.parent = parent
		self.g = g
		self.h = h
		self.f = g+h
	def __lt__(self,other):
		return self.f < other.f
		
def a_star_search(start,goal,heuristic,graph):
	open_list = []
	closed_list = set()
	
	start_node = Node(start,g=0,h = heuristic[start])
	heapq.heappush(open_list,start_node)
	
	while open_list:
		current_node = heapq.heappop(open_list)
		
		if current_node.state == goal:
			path = []
			
			while current_node:
				path.append(current_node.state)
				current_node = current_node.parent
			return path[::-1]
			
		closed_list.add(current_node.state)
		
		for neighbor,cost in graph[current_node.state]:
			if neighbor in closed_list:
				continue
			g = current_node.g + cost
			h = heuristic[neighbor]
			
			neighbor_node = Node(neighbor,parent=current_node,g=g,h=h)
			
			if not any(node.state == neighbor and node.f <= neighbor_node.f for node in open_list):
				heapq.heappush(open_list,neighbor_node)
	return None
	
graph = {
	'A':[('B',1),('C',4)],
	'B':[('C',2),('D',5)],
	'C':[('D',1)],
	'D':[]
}


heuristic = {
	'A':7,
	'B':6,
	'C':2,
	'D':0
}

start = 'A'
goal = 'D'
path = a_star_search(start, goal, heuristic, graph)

print("Path found:", path)
