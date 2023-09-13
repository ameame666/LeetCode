# https://leetcode.cn/problems/trapping-rain-water/
# 用两个指针相向而行，在用两个变量记录当前位置左侧和右侧的最大高度，那么能存储的水量就是max-heigh[i]，时间复杂度O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        lh, rh = 0, 0
        l, r = 0, len(height)-1
        while l < r:
            lh = max(lh, height[l])
            rh = max(rh, height[r])
            if lh < rh:
                res += lh - height[l]
                l += 1
            else:
                res += rh - height[r]
                r -= 1
        return res