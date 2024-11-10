from sys import maxsize
from itertools import permutations
V = 4
graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
s = 0
def travellingSalesmanProblem(graph, s):
	vertex = []
	for i in range(V):

		if i != s:
			#print (i)
			vertex.append(i)
			#print(vertex)

	min_path = maxsize
	best_tour= None

	next_permutation=permutations(vertex)

	for i in next_permutation:
		#print(i)

		current_pathweight = 0
		k = s

		for j in i:

			current_pathweight += graph[k][j]
			#print(current_pathweight)
			k = j

		current_pathweight += graph[k][s]
		#print("weight=",current_pathweight)
		if current_pathweight < min_path:
			min_path = min(min_path, current_pathweight)

			best_tour = [s] + list(i) + [s]

	return min_path,best_tour
min_path,best_tour=(travellingSalesmanProblem(graph, s))
print('min_path=',min_path)
print('best_tour=',best_tour)
