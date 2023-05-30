def prims_mst(maze):
  """Generates a perfect maze using Prim's MST algorithm and prints the coordinates of the end node.

  Args:
    maze: A 2D array of integers, where each integer represents a cell in the maze.

  Returns:
    A 2D array of integers, where each integer represents a cell in the maze.
  """

  # Create a graph with one node for each cell in the maze.
  graph = {}
  for i in range(len(maze)):
    for j in range(len(maze[0])):
      graph[(i, j)] = []

  # Connect each pair of nodes that are adjacent in the maze.
  for i in range(len(maze) - 1):
    for j in range(len(maze[0]) - 1):
      if maze[i][j] == 1 and maze[i + 1][j] == 1:
        graph[(i, j)].append((i + 1, j))
      if maze[i][j] == 1 and maze[i][j + 1] == 1:
        graph[(i, j)].append((i, j + 1))

  # Choose any node to be the starting node.
  start_node = (0, 0)

  # Repeat the following steps until all nodes have been visited:
  visited = set()
  while len(visited) < len(graph):
    # Find the edge with the smallest weight that connects a node in the MST to a node that is not in the MST.
    minimum_edge = None
    for node, edges in graph.items():
      if node not in visited:
        for edge in edges:
          if edge not in visited:
            if minimum_edge is None or graph[node][edge] < graph[minimum_edge][edge]:
              minimum_edge = (node, edge)

    # Add the edge to the MST.
    graph[minimum_edge[0]].remove(minimum_edge[1])
    graph[minimum_edge[1]].remove(minimum_edge[0])
    visited.add(minimum_edge[0])
    visited.add(minimum_edge[1])

  # The resulting graph is a perfect maze.
  return graph

  # Print the coordinates of the end node.
  end_node = next(node for node, edges in graph.items() if len(edges) == 0)
  print(end_node)
