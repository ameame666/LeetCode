# 中心扩散法 时间复杂度是O(N^2)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def Palindrome(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        res = ''
        for i in range(len(s)):
            s1 = Palindrome(i, i)
            s2 = Palindrome(i, i+1)
            if len(s1) > len(res):
                res = s1
            if len(s2) > len(res):
                res = s2
        return res