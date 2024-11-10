graph = {
    'a' : ['b','c'],
    'b' : ['a','c','d'],
    'c' : ['a','b','d'],
    'd' : ['b','c']
}

visited = []
queue = []

def bfs(visited, graph, startnode, goalnode):
  flag = 0
  visited.append(startnode)
  queue.append(startnode)
  while queue:
    m = queue.pop(0)
    for neighbour in graph[m]:
      if flag == 0:
        if neighbour not in visited:
          visited.append(neighbour)
          queue.append(neighbour)
          print("visited",visited)
          if neighbour == goalnode:
            print("goal reached")
            print("Path taken is",visited)
            flag = 1
            
    if flag == 0:
      print("goal not reached")

print("BFS")
bfs(visited, graph, 'a', 'd')
