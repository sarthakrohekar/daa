def dfs(graph, node, visited, order):
    if node not in visited:
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited, order)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start = 'A'
visited = set()
order = []
dfs(graph, start, visited, order)
print("DFS Traversal Order:", order)
print("Total Nodes Visited:", len(visited))