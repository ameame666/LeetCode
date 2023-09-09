# https://leetcode.cn/problems/max-area-of-island/
# dfs,计算是用淹岛屿方法计算，如果是0返回，是1进行计算，用一个area来进行记录，而不是使用回溯
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            area = 1
            directions = [[0,1],[1,0],[0,-1],[-1,0]]
            for x, y in directions:
                area += dfs(i+x, j+y)
            return area
        
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = max(area, dfs(i, j))
        
        return area