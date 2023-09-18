"""
小美拿到了一个排列。她想知道在这个排列中，x和y是否是相邻的。你能帮帮她吗？
排列是指一个长度为n的数组，其中 1 到n每个元素恰好出现一次。

输入描述：
第一行输入一个正整数n，代表排列的长度。
第二行输入n个正整数a_i，代表排列的元素。
第三行输入两个正整数x和y，用空格隔开。

输出描述：
如果x和y在排列中相邻，则输出"Yes"。否则输出"No"
"""

n = int(input())
nums = list(map(int, input().split()))
x, y = map(int, input().split())

index_x = nums.index(x)
index_y = nums.index(y)

if abs(index_x - index_y) == 1:
    print('Yes')
else:
    print('No')