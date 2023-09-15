# https://leetcode.cn/problems/longest-substring-without-repeating-characters/
# 滑动窗口求解，left和right指针从后向前遍历，res记录最大结果
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windows = {}
        res = 0
        left, right = 0, 0
        while right < len(s):
            c = s[right]
            windows[c] = windows.get(c, 0) + 1
            right += 1

            while windows[c] > 1:
                d = s[left]
                windows[d] -= 1
                left += 1
            res = max(res, right - left)
        return res