def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend([neighbor for neighbor in graph[vertex] if neighbor not in visited])

# Đồ thị
graph = {
    'S': ['A','B'],
    'A': ['C','D','S','G'],
    'B': ['C'],
    'C': ['G', 'A'],
    'D': ['G'],
    'G': ['C','D']
}

bfs(graph, 'S')
