
def dfs(start, adj, vis, dfs_list):
    vis[start] = 1
    dfs_list.append(start)

    for x in adj[start]:
        if not vis[x]:
            dfs(x, adj, vis, dfs_list)


def main():
    adj = [[1, 2], [0, 2, 3], [0, 4], [1, 4], [2, 3]]
    visited = [0 for _ in range(len(adj))]
    dfs_list = []
    dfs(0, adj, visited, dfs_list)
    print(dfs_list)
main()