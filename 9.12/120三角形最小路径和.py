# https://leetcode.cn/problems/triangle/
# 创建一个二维数组， 存储最顶层到最底层的最短路径长度，注意用逆向思维，第[i][j]位置只有可能是[i-1][j],[i-1][j-1]位置到来的，时间，空间复杂度O(n*2)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[float('inf')] * len(triangle) for _ in range(len(triangle))]
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
                else:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
        res = float('inf')
        for i in range(len(dp[len(dp)-1])):
            res = min(res, dp[len(dp)-1][i])
        
        return res

# 优化版本，自底往上找，空间复杂度降到O(n)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * len(triangle)
        for i in range(len(triangle[len(triangle)-1])):
            dp[i] = triangle[len(triangle)-1][i]
        
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        
        return dp[0]