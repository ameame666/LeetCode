# https://leetcode.cn/problems/ransom-note/
# 使用字典来存储magzine中字母出现的次数，注意这里一个字母只能用一次，所以不能用集合
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charcount = {}
        for c in magazine:
            charcount[c] = charcount.get(c, 0) + 1

        for c in ransomNote:
            if c in charcount and charcount[c] >= 1:
                charcount[c] -= 1
            else:
                return False

        return True 