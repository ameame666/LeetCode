# 整数反转 https://leetcode.cn/problems/reverse-integer/description/ 

class Solution:
    def reverse(self, x: int) -> int:
        upbound = 2**31 - 1
        lowbound = -2**31
        sign = 1 if x > 0 else -1
        res = 0
        x = abs(x)
        while x != 0:
            last = x % 10
            x = x // 10
            if res > upbound // 10 or (res == upbound // 10 and last > 7):
                return 0
            if res < lowbound // 10 or (res == lowbound // 10 and last > 8):
                return 0
            res = res * 10 + last
        return sign * res