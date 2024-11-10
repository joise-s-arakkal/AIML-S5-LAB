import heapq
class Node:
	def __init__(self, state, parent = None, cost = 0):
		self.state = state
		self.parent = parent
		self.cost = cost
		
	def __lt__(self,other):
		return self.cost < other.cost
			
def best_first_search(start, goal, heuristic, graph):
	open_list = []
	closed_list = set()
			
	start_node = Node(start,cost = heuristic[start])
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
				
				
		for neighbor in graph[current_node.state]:
			if neighbor in closed_list:
				continue
				
			neighbor_node = Node(neighbor, parent = current_node, cost= heuristic[neighbor])
			
			if not any(node.state == neighbor for node in open_list):
				heapq.heappush(open_list,neighbor_node)
	return None

graph = {

	'A':['B','C'],
	'B':['D','E'],
	'C':['F'],
	'D':[],
	'E':['F'],
	'F':['G'],
	'G':[]
}

heuristic = {
	'A':6,
	'B':5,
	'C':4,
	'D':7,
	'E':3,
	'F':2,
	'G':0
}

start = 'A'
goal = 'G'

path = best_first_search(start,goal,heuristic,graph)

print("Path found:",path)
