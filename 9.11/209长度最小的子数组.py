# https://leetcode.cn/problems/minimum-size-subarray-sum/
# 滑动指针问题，用双指针遍历，用一个变量记录左右之间的数的和，然后不断移动指针记录最小长度
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        numsum = 0
        left, right = 0, 0
        while right < len(nums):
            numsum += nums[right]
            while numsum >= target:
                res = min(res, right-left+1)
                numsum -= nums[left]
                left += 1
            right += 1
        return 0 if res == float('inf') else res
