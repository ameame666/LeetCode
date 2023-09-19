# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description/
# 一个长度为价格的二维矩阵解决，时空复杂度都是O(n)，可以优化空间复杂度，用两个常数记录最终结果
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][0], dp[0][1] = 0, -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        return dp[len(prices)-1][0]