def dfs(pos, grid, vis):
    (row, col) = pos
    vis[row][col] = 1
    dx = [0, +1, 0, -1]
    dy = [-1, 0, +1, 0]

    for i in range(4):
        newRow = row + dx[i]
        newCol = col + dy[i]

        if (newRow < len(grid) and newRow >= 0 and newCol < len(grid[0]) and newCol >= 0 and grid[newRow][
            newCol] == "1" and vis[newRow][newCol] == 0):
            dfs((newRow, newCol), grid, vis)


def numIslands(grid):
    vis = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if vis[i][j] == 0 and grid[i][j] == "1":
                cnt += 1
                dfs((i, j), grid, vis)
    return cnt

def main():
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(numIslands(grid))
main()