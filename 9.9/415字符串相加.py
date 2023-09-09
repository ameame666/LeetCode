# 让两个指针从后往前走就可以，用一个carry记录进位，时空复杂度都是O(max(M, N))
# https://leetcode.cn/problems/add-strings/description/
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        e1, e2 = len(num1)-1, len(num2)-1
        carry = 0
        while e1 >= 0 and e2 >= 0:
            res.append((int(num1[e1]) + int(num2[e2]) + carry) % 10)
            carry = (int(num1[e1]) + int(num2[e2]) + carry) // 10
            e1 -= 1
            e2 -= 1
        
        while e1 >= 0:
            res.append((int(num1[e1]) + carry) % 10)
            carry = (int(num1[e1]) + carry) // 10
            e1 -= 1
            
        while e2 >= 0:
            res.append((int(num2[e2]) + carry) % 10)
            carry = (int(num2[e2]) + carry) // 10
            e2 -= 1
        
        if carry != 0:
            res.append(carry)
        
        return ''.join(str(x) for x in res[::-1])
