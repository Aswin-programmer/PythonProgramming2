class Solution:

    def dfs(self, node, s, visited, adj_list):
        visited[node] = 1

        for adj_node in adj_list[node]:
            if visited[adj_node] == 0:
                self.dfs(adj_node, s, visited, adj_list)
        s.insert(0, node) #The replaces the use of popping of stack which we used to do with our c++ code.

    def topo_sort(self, adj_list):
        visited = [0 for _ in range(len(adj_list))]
        s = []

        for k in range(len(adj_list)):
            if visited[k] == 0:
                self.dfs(k, s, visited, adj_list)
        return s

def main():
    sol = Solution()
    adj_list = {
        0: [],
        1: [3],
        2: [3],
        3: [],
        4: [1, 0],
        5: [0, 2]
    }

    print(sol.topo_sort(adj_list))
main()