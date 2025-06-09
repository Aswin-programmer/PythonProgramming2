def orangesRotting(grid):
    visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    queue = []

    cnt_fresh = 0
    cnt_fresh_check = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 2:
                queue.append(((row, col), 0))
            if grid[row][col] == 1:
                cnt_fresh += 1

    time = -1e9

    while (len(queue) != 0):
        ((r, c), t) = queue.pop(0)
        time = max(time, t)

        dx = [0, +1, 0, -1]
        dy = [-1, 0, +1, 0]

        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if (nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and visited[nr][nc] == 0 and grid[nr][
                nc] == 1):
                visited[nr][nc] = 1
                queue.append(((nr, nc), t + 1))
                cnt_fresh_check += 1

    if cnt_fresh_check != cnt_fresh:
        return -1
    else:
        return time


def main():
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(orangesRotting(grid))
main()





