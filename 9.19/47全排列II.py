# https://leetcode.cn/problems/permutations-ii/description/
# 包含重复元素但是不可复选，要避免选到同一个元素的情况，用used标记，为了防止出现重复情况，要进行剪枝，如果是相同元素，前一个元素没使用的情况下，当前元素不能使用
# 时间复杂度是 O(N*N!)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []
        used = [False] * len(nums)
        nums.sort()
        
        def backtrack():
            if len(track) == len(nums):
                res.append(track.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                track.append(nums[i])
                used[i] = True
                backtrack()
                used[i] = False
                track.pop()
        
        backtrack()
        return res