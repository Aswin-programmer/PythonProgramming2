class Solution(object):
    def possibleBipartition(self, n, dislikes):
        adj_list = [[] for _ in range(n)]
        visited = [-1 for _ in range(n)]

        for dislike in dislikes:
            adj_list[dislike[0] - 1].append(dislike[1] - 1)
            adj_list[dislike[1] - 1].append(dislike[0] - 1)

        queue = []
        queue.append(0)
        visited[0] = 0

        while len(queue) != 0:
            node = queue.pop(0)

            for adj_node in adj_list[node]:
                if visited[adj_node] == -1:
                    visited[adj_node] = 1 if visited[node] == 0 else 0
                    queue.append(adj_node)
                else:
                    if visited[adj_node] == visited[node]:
                        return False
        return True


#https://leetcode.com/problems/possible-bipartition/