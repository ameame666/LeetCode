# https://leetcode.cn/problems/house-robber/
# 简单的一维dp，注意可以优化空间复杂度到O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        pre = nums[0]
        cur = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nxt = max(cur, pre+nums[i])
            pre = cur
            cur = nxt