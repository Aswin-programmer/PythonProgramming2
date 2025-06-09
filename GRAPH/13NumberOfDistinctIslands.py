# User function Template for python3

import sys
from typing import List

sys.setrecursionlimit(10 ** 8)


class Solution:

    def dfs(self, start, end, start_i, end_i, visited, grid, l):
        visited[start][end] = 1

        l.append((start - start_i, end - end_i))

        dx = [0, +1, 0, -1]
        dy = [-1, 0, +1, 0]

        for i in range(4):
            new_r = start + dx[i]
            new_c = end + dy[i]
            if (new_r < len(grid) and new_r >= 0 and new_c < len(grid[0]) and new_c >= 0 and grid[new_r][new_c] == 1 and
                    visited[new_r][new_c] == 0):
                self.dfs(new_r, new_c, start_i, end_i, visited, grid, l)

    def countDistinctIslands(self, grid: List[List[int]]) -> int:
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        l = []
        s = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == 0 and grid[i][j] == 1:
                    self.dfs(i, j, i, j, visited, grid, l)
                    s.add(tuple(l))
                    l = []
        return len(s)

def main():
    s = Solution()
    grid = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1]
    ]
    print(s.countDistinctIslands(grid))
main()












