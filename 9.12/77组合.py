# https://leetcode.cn/problems/combinations/
# 回溯算法，设立start，时间复杂度O(2^k)，注意加一个return进行剪枝可以减少消耗时间
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        track = []
        def backtrack(start):
            if len(track) == k:
                res.append(track.copy())
                return
            for i in range(start, n+1):
                track.append(i)
                backtrack(i+1)
                track.pop()
        
        backtrack(1)
        return res