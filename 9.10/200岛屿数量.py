# https://leetcode.cn/problems/number-of-islands/
# dfs淹岛屿，每次发现一片岛屿，岛屿数量加一，用dfs淹掉和他相邻的陆地，时间复杂度是 O(m * n)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] == '0':
                return
            grid[i][j] = '0'
            directions = [[0,1],[1,0],[0,-1],[-1,0]]
            for x, y in directions:
                dfs(x+i, y+j)
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res