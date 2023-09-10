# https://leetcode.cn/problems/coin-change
# 自低向上，用一个dp数组存储一个不可能得到的结果，注意判断数组越界，时间复杂度O(amount*len(coins))，空间复杂度O(amount)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i-coin]+1)
        if dp[amount] == amount+1:
            return -1
        return dp[amount]