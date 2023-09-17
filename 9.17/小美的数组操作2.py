"""
小美拿到了一个数组，她每次可以进行如下操作：
选择两个元素，一个加 1，另一个减 1。
小美总共进行了k次操作。她希望你回答最终数组是否是非降序，你能帮帮她吗？
请注意，元素可能会被减成负数！

输入描述：
第一行输入一个正整数 t，代表询问次数。
每次询问首先第一行输入两个正整数n和k，代表数组长度和操作次数。
接下来的一行输入n个正整数 a_i，代表初始数组。
接下来的k行，每行输入两个正整数u,v，代表使得第u个元素加 1，第v个元素减 1。

输出描述
输出t行，每行输出该次询问的答案。
如果数组变成了非降序，则输出"Yes"。否则输出 "No"。
"""

# 模拟题
t = int(input())

def judge(nums):
    for i in range(1, len(nums)):
        if nums[i] >= nums[i-1]:
            continue
        else:
            return 'No'
    return 'Yes'

for i in range(t):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    for i in range(k):
        u, v = map(int, input().split())
        nums[u-1] += 1
        nums[v-1] -= 1
    print(judge(nums))
