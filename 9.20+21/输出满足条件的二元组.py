"""
现在有一个长度为n的序列a_1,a_2,...a_n，给定一个整数k，需要求出满足如下条件的二元组（i,j）：
1. i<j
2. |a_i+a_j-k|最小
现在希望输出满足条件的最小值和满足条件的二元组个数，输入是n和序列数组nums
"""

# 注意这儿是绝对值即可，可以直接暴力计算，先求出|a_i+a_j-k|，然后遍历计数，不过也没想到更好的方法
n, k = map(int, input().split())
nums = list(map(int, input().split()))
numsum = []

for i in range(n):
    for j in range(i+1, n):
        numsum.append(nums[i]+nums[j])
numsum.sort()

minsum = float('inf')
for num in numsum:
    minsum = min(minsum, abs(num - k))

res = []
for i in range(n):
    for j in range(i+1, n):
        if abs(nums[i] + nums[j] -k) == minsum:
            res.append((i, j))

print(minsum, len(res))