# https://leetcode.cn/problems/container-with-most-water/description/
# 双指针解法，能盛水的面积就是(right - left)*min(height[right], height[left])，时间复杂度O(N)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height)-1
        while left < right:
            res = max(res, (right - left)*min(height[right], height[left]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res