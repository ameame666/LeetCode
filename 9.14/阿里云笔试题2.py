# 题目: 构造一个长度为n，每个数都不超过m的全为正数的数组，使数组中没有相邻元素的按位与等于0，求有多少个数组满足要求
# 相邻元素按位与j & k
def countArrays(n, m):
    MOD = 10**9 + 7
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    # 初始化边界情况
    for j in range(1, m+1):
        dp[1][j] = 1
    
    # 动态规划
    for i in range(2, n+1):
        for j in range(1, m+1):
            for k in range(1, m+1):
                if (j & k) != 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
    
    # 计算总数量
    total = sum(dp[n]) % MOD
    return total
