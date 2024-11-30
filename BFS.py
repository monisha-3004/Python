import collections

def bfs(graph,root):
    visited,queue = set(),collections.deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
    print(str(vertex)+" ",end=" ")
    for neighbour in graph[vertex]:
        if neighbour not in visited:
             visited.add(neighbour)
        queue.append(neighbour)

if __name__ == '__main__':
    graph = {0:[1,3],1:[2],2:[0],3:[1]}
print("following is Breadth First Traversed:")
bfs(graph,1)
        
