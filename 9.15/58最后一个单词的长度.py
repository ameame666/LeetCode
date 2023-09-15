# https://leetcode.cn/problems/length-of-last-word/
# 去除首尾字符串进行遍历即可
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        right = len(s) - 1
        while right >= 0 and s[right] != ' ':
            right -= 1
        return len(s) - right - 1