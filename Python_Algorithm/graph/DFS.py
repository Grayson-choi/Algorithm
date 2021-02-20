graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def recursive_dfs(v, visited=[]):
    visited.append(v)
    for w in graph[v]:
        if not w in visited:
            visited = recursive_dfs(w, visited)
    return visited

print(f'recursive dfs: {recursive_dfs(1)}')