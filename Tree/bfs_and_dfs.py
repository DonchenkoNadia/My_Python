from collections import deque
graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D", "E"],
        "D": ["B", "C"],
        "E": ["C", "F"],
        "F": ["E", "O", "I", "G"],
        "G": ["F", "H"],
        "H": ["G"],
        "I": ["F", "J"],
        "O": ["F"],
        "J": ["K", "L", "I"],
        "K": ["J"],
        "L": ["J"],
        "P": ["Q", "R"],
        "Q": ["P", "R"],
        "R": ["P", "Q"],
}
tests = [
        ("A", "L", True),
        ("A", "B", True),
        ("H", "K", True),
        ("L", "D", True),
        ("P", "Q", True),
        ("Q", "P", True),
        ("Q", "G", False),
        ("R", "A", False),
        ("P", "B", False),
        ("E", "H", True),
        ("L", "R", False)
]

def isRoute(start, end, visited = None):
    if visited == None:
        visited = set()
    for node in graph.get(start, []):
        if node not in visited:
            visited.add(node)
            if node == end or isRoute(node, end, visited):
                return True


    return False

def isRouteBFS(start, end):
    if start == end:
        return True
    visited = set()
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                if neighbor == end:
                    return True
    return False


k = 0
for test in tests:
    k += 1
    if isRouteBFS(test[0], test[1]) == test[2]:
        print(f"test {k} is passed")
    else:
        print(f"test {k} is not passed")
