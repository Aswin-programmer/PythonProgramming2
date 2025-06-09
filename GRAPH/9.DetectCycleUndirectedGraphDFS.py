class Solution:

    def DFS(self, node, parent, visited, adj_list):
        visited[node] = 1
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                if self.DFS(neighbor, node, visited, adj_list):
                    return True
            elif neighbor != parent:
                return True
        return False

    def isCycle(self, V, edges):
        adj_list = [[] for _ in range(V)]
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        visited = [0] * V

        for node in range(V):
            if not visited[node]:
                if self.DFS(node, -1, visited, adj_list):
                    return True
        return False


def main():
    sol = Solution()
    print(sol.isCycle(5, [(0, 1), (1, 2), (2, 0), (3, 4)]))  # True: cycle in 0-1-2
    print(sol.isCycle(3, [(0, 1), (1, 2)]))                 # False: no cycle


main()
