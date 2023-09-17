"""
小美拿到了一个数组a，她准备构造一个数组
b满足：
1. b的每一位都和a对应位置不同
2. b的所有元素之和都和a相同。
3. b的数组均为正整数。
请你告诉小美有多少种构造方式。由于答案过大，请对结果按10**9+7取模

输入描述：
第一行输入一个正整数n，代表数组的大小。
第二行输入n个正整数a_i，代表小美拿到的数组。
输出描述:
一个整数
"""
# 没有思路
# 动态规划? pypy3运行可以通过
MOD = 10**9 + 7

n = int(input())
a = list(map(int, input().split()))
sum_a = sum(a)

# 构成 [和为s,前n个元素] 的可能数
dp = [[0] * (n + 1) for _ in range(sum_a + 1)]
dp[0][0] = 1

for s in range(1, sum_a + 1):
    for l in range(1, n + 1):
        cnt = 0
        # 前面的和至少为l-1
        for ps in range(l - 1, s):
            if s - ps == a[l - 1]:
                continue
            prev_cnt = dp[ps][l - 1]
            cnt = (cnt + prev_cnt) % MOD
        dp[s][l] = cnt

print(dp[sum_a][n])

