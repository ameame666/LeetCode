"""
题目：
小美拿到了一个数组，她每次可以进行如下操作：
选择两个元素，一个加 1，另一个减 1。
小美希望若干次操作后，众数的出现次数尽可能多。你能帮她求出最小的操作次数吗？
第一行为一个正整数n，代表数组的大小。
第二行输入n个正整数a_i，代表小美拿到的数组。
"""

# 要使众数最多，那么数量不是n就是n-1。
# 当sum能整除n时，一定可以使所有数变成同一个数，就是平均数，直接计算即可。
# 否则，可以尝试把其中n-1个变成一样的，另一个数承载垃圾操作。那么这个数一定是最大的数或者最小的数。
# 那目标数字应该是这n-1个数的平均数，步数才是最小的。注意这个数可能不是整数，s/t,s/t+1都试试。

n = int(input())
nums = list(map(int, input().split()))
s = sum(nums)

if s % n == 0:
    count = 0
    for num in nums:
        count += abs(s//n - num)
    print(count // 2)

else:
    nums.sort()
    s1 = s - nums[0]
    s2 = s - nums[-1]
    def getcount(nums, mean):
        left, right = 0, 0
        for num in nums:
            if num <= mean:
                left += mean - num
            else:
                right += num - mean
        return max(left, right)
    p1 = getcount(nums[1:], s1 // (n-1))
    p2 = getcount(nums[1:], s1 // (n-1)+1)
    p3 = getcount(nums[:-1], s2 // (n-1))
    p4 = getcount(nums[:-1], s2 // (n-1)+1)
    print(min(p1, p2, p3, p4))


