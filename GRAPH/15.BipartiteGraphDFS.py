class Solution(object):

    def dfs(self, index, color, visited, adj_list):
        visited[index] = color

        for node in adj_list[index]:
            if visited[node] == -1:
                if (self.dfs(node, 0 if visited[index] == 1 else 1, visited, adj_list) == False):
                    return False
            else:
                if visited[index] == visited[node]:
                    return False
        return True

    def possibleBipartition(self, n, dislikes):
        adj_list = [[] for _ in range(n)]
        visited = [-1 for _ in range(n)]

        for dislike in dislikes:
            adj_list[dislike[0] - 1].append(dislike[1] - 1)
            adj_list[dislike[1] - 1].append(dislike[0] - 1)

        for k in range(n):
            if visited[k] == -1:
                if self.dfs(k, 0, visited, adj_list) == False:
                    return False
        return True


