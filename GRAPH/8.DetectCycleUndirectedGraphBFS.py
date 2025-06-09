class Solution:
    def C(self, queue, visited, adj_list):
        while queue:
            node, parent = queue.pop(0)

            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = 1
                    queue.append((neighbor, node))
                elif neighbor != parent:
                    return True
        return False

    def isCycle(self, V, edges):
        adj_list = [[] for _ in range(V)]
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        visited = [0 for _ in range(V)]

        for node in range(V):
            if not visited[node]:
                queue = [(node, -1)]
                visited[node] = 1
                if self.C(queue, visited, adj_list):
                    return True
        return False

def main():
    sol = Solution()
    print(sol.isCycle(5, [(0, 1), (1, 2), (2, 0), (3, 4)]))  # Output: True (cycle exists)
    print(sol.isCycle(3, [(0, 1), (1, 2)]))  # Output: False (no cycle)
main()