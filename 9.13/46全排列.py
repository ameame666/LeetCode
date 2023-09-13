# https://leetcode.cn/problems/permutations/
# 回溯算法，注意用一个used判断这个数是否使用过
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []
        used = [False] * len(nums)

        def backtrack():
            if len(track) == len(nums):
                res.append(track.copy())
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    track.append(nums[i])
                    backtrack()
                    used[i] = False
                    track.pop()
        
        backtrack()
        return res