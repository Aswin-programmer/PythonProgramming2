# Implementing using the list
def BFS_Using_List():
    adj = [[1,2], [0,2,3], [0,4], [1,4], [2,3]]
    visited = [0 for _ in range(len(adj))]

    queue = []
    queue.append(0)
    visited[0] = 1

    bfs = []

    while (len(queue) != 0):
        node = queue.pop(0)
        bfs.append(node)

        for x in adj[node]:
            if not visited[x]:
                queue.append(x)
                visited[x] = 1

    return bfs

# Implementing using the deque

from collections import deque
def BFS_Using_Deque():
    adj = [[1, 2], [0, 2, 3], [0, 4], [1, 4], [2, 3]]
    visited = [0 for _ in range(len(adj))]

    queue = deque()
    queue.append(0)
    visited[0] = 1

    bfs = []

    while (len(queue) != 0):
        node = queue.popleft()
        bfs.append(node)

        for x in adj[node]:
            if not visited[x]:
                queue.append(x)
                visited[x] = 1
    return bfs

def main():
    print(BFS_Using_List())
    print(BFS_Using_Deque())
main()