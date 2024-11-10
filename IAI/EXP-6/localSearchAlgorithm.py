import random
class MapColoringLocalSearch:
	def __init__(self, graph, colors):
		self.graph = graph # adjacency list representing the map
		self.colors = colors # list of available colors
		self.num_regions = len(graph)
		self.color_assignment = {}
		
	# Randomly assign colors to each region
	def random_initial_assignment(self):
		for region in self.graph:
			self.color_assignment[region] = random.choice(self.colors)
	# Calculate number of conflicts
	def calculate_conflicts(self):
		conflicts = 0
		for region in self.graph:
			for neighbor in self.graph[region]:
				if self.color_assignment[region] == self.color_assignment[neighbor]:
					conflicts += 1
		return conflicts

	# Try to minimize conflicts
	def solve(self, max_iterations=1000):

		self.random_initial_assignment()
		current_conflicts = self.calculate_conflicts()
		for i in range(max_iterations):
			if current_conflicts == 0:
				print(f"Solution found in {i} iterations!")
				return self.color_assignment
				
			# Pick a random region involved in a conflict
			region = random.choice(list(self.graph.keys()))
			# Try to change its color to reduce conflicts
			best_color = self.color_assignment[region]
			min_conflicts = current_conflicts
			for color in self.colors:
				if color != self.color_assignment[region]:
					self.color_assignment[region] = color
					conflicts = self.calculate_conflicts()
					if conflicts < min_conflicts:
						min_conflicts = conflicts
						best_color = color
			self.color_assignment[region] = best_color
			current_conflicts = min_conflicts
		print("No solution found after maximum iterations")
		return self.color_assignment
# Example map (graph) with 4 regions and borders between them
graph = {
'A': ['B', 'C', 'D'],
'B': ['A', 'C'],
'C': ['A', 'B', 'D'],
'D': ['A', 'C']
}

# List of available colors
colors = ['Red', 'Green', 'Blue']
# Initialize the local search algorithm
solver = MapColoringLocalSearch(graph, colors)
# Solve the map coloring problem
solution = solver.solve()
# Print the solution (color assignment)
print("Color assignment:", solution)
