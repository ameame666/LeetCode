# https://leetcode.cn/problems/combination-sum/
# 回溯算法，注意要避开重复结果的计算，输入start来限制candidates中能选择的元素
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        track = []
        def backtrack(start):
            if sum(track) == target:
                res.append(track.copy())
                return
            if sum(track) > target:
                return
            for i in range(start, len(candidates)):
                track.append(candidates[i])
                backtrack(i)
                track.pop()
        
        backtrack(0)
        return res