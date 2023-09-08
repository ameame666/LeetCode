# dfs再加回溯，和岛屿问题很像，注意用onpath来防止走到重复路径，用pathsum和res比较来获得结果

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i, j, pathsum):
            nonlocal res
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if onpath[i][j]:
                return
            if grid[i][j] == 0:
                return
            directions = [[0,1], [1,0], [-1,0], [0,-1]]
            onpath[i][j] = True
            pathsum += grid[i][j]
            res = max(pathsum, res)

            for x, y in directions:
                dfs(i+x, j+y, pathsum)
            
            onpath[i][j] = False
            pathsum -= grid[i][j]
        
        res = 0
        onpath = [[False] * len(grid[0]) for _ in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dfs(i, j, 0)
        
        return res