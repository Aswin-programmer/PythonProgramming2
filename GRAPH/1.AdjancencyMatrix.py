################ ADJACENCY MATRIX #############################
def adjancency_matrix():
    n = 5
    e = 6
    edge_list = [(1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 5)]#This is the actual node value and not the indices.
    #edge_list = [(0, 1), (0, 2), (1, 3), (2, 3), (2, 4), (3, 4)]#This is the actual node value and not the indices.
    adj = [[0 for _ in range(n+1)] for _ in range(n+1)] #Adjancency Matrix

    for (x, y) in edge_list:
        adj[x][y] = 1
        adj[y][x] = 1

    print(adj)

################ ADJACENCY LIST #############################
def adjancency_list():
    n = 5
    e = 6
    edge_list = [(1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 5)]
    adj = [[] for _ in range(n+1)]

    for (x, y) in edge_list:
        adj[x].append(y)
        adj[y].append(x)

    print(adj)

def main():
    adjancency_list()
main()