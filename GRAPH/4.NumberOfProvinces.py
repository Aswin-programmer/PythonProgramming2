#https://leetcode.com/problems/number-of-provinces/

class Solution(object):

    def dfs(self, start, adj, vis):
        vis[start] = 1

        for x in adj[start]:
            if not vis[x]:
                self.dfs(x, adj, vis)

    def findCircleNum(self, isConnected):
        adj = [[] for _ in range(len(isConnected))]
        vis = [0 for _ in range(len(isConnected))]

        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if (i != j and isConnected[i][j] == 1):
                    adj[i].append(j)
                    adj[j].append(i)
        cnt = 0
        for node in range(len(isConnected)):
            if not vis[node]:
                cnt += 1
                self.dfs(node, adj, vis)
        return cnt



