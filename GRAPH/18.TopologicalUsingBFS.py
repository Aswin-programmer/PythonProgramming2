class Solution:

    def topo_sort(self, adj_list):
        s = []

        indegree = [0 for _ in range(len(adj_list))]
        for node in range(len(adj_list)):
            for adj_node in adj_list[node]:
                indegree[adj_node] += 1

        queue = []
        for k in range(len(adj_list)):
            if indegree[k] == 0:
                queue.append(k)

        while (len(queue) != 0):
            node = queue.pop(0)
            s.append(node)

            for adj_node in adj_list[node]:
                indegree[adj_node] -= 1

                if indegree[adj_node] == 0:
                    queue.append(adj_node)
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