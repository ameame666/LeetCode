# https://leetcode.cn/problems/longest-common-prefix/
# 类似于一个二维数组的遍历问题，注意判断语句怎么写，时间复杂度O(n^2)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                pre = strs[j-1]
                cur = strs[j]
                if i >= len(pre) or i >= len(cur) or pre[i] != cur[i]:
                    return strs[j][:i]
        return strs[0]

