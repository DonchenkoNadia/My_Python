graph = {
    "A" : ["B", "C"],
    "B" : ["A"],
    "C" : ["A"],
    "D" : []
}
def is_route(graph, start, end, visited = None):
    if visited is None:
        visited = set()
    for node in graph[start]:
        if node not in visited:
            visited.add(node)
            if node == end or is_route(graph, node, end, visited):
                return True
    return False

print (is_route(graph, "B", "D"))
