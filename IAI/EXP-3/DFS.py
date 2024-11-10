graph = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}


visited = []
def dfs(visited, graph, startnode, goalnode):
  flag = 0
  if startnode not in visited:
    visited.append(startnode)
    if startnode == goalnode:
      flag = 1
      print("goal is reached")
      print("Path taken to reach the goal is",visited)
      
    elif flag == 0:
      for neighbour in graph[startnode]:
        dfs(visited, graph, neighbour, goalnode)

  elif flag == 0:
    print("goal not reached")

print("DFS")
dfs(visited, graph, '5', '7')


  
