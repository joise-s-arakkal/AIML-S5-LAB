def is_safe_csp(node, color, graph, assignment):
	"""
	Check if assigning color to node is safe, i.e.,
	no adjacent node has the same color.
	"""
	for neighbor in graph[node]:
		if neighbor in assignment and assignment[neighbor] == color:
			return False
	return True
	
def select_unassigned_variable(graph, assignment):
	"""
	Select the next unassigned variable (node) for coloring.
	This can be done with various heuristics; here we simply
	select the first unassigned variable.
	"""
	for node in graph:
		if node not in assignment:
			return node
	return None
	
def backtracking_search_csp(graph, colors, assignment):
	"""
	Backtracking search algorithm for solving the map coloring problem using CSP.
	graph: Adjacency list representation of the graph (map).
	colors: List of available colors.
	assignment: A dictionary storing the current color assignment for each node.
	"""
	# If all regions (nodes) are assigned, return the solution
	if len(assignment) == len(graph):
		return assignment
		
	# Select an unassigned variable (node)
	node = select_unassigned_variable(graph, assignment)
	# Try each color for the current node
	for color in colors:
		if is_safe_csp(node, color, graph, assignment):

			# Assign the color
			assignment[node] = color
			# Recursively try to color the remaining nodes
			result = backtracking_search_csp(graph, colors, assignment)
			if result:
				return result
			# If no valid solution, backtrack
			del assignment[node]
	# No valid color could be assigned, return failure (None)
	return None
	
def solve_map_coloring_csp(graph, num_colors):
	"""
	Solve the map coloring problem using backtracking search with CSP.
	graph: Adjacency list representation of the map.
	num_colors: Number of available colors.
	"""
	# Define the available colors
	colors = list(range(1, num_colors + 1))
	# Initialize assignment (empty)
	assignment = {}
	# Perform backtracking search
	solution = backtracking_search_csp(graph, colors, assignment)
	if solution:
		print("Solution exists! Color assignment:")
		print(solution)
	else:
		print("No solution exists with the given number of colors.")
		
		
# Example usage
if __name__ == "__main__":
	# Define the adjacency list for the graph (map)
	# Example: A graph with 4 regions (0, 1, 2, 3) and edges representing adjacency
	graph = {
	0: [1, 2],
	1: [0, 2, 3],
	2: [0, 1, 3],
	3: [1, 2]
	}
	# Define the number of colors
	num_colors = 3
	# Solve the map coloring problem using CSP backtracking
	solve_map_coloring_csp(graph, num_colors)
