"""
小美定义一个 01 串的权值为：每次操作选择一位取反，使得相邻字符都不相等的最小操作次数。
例如，"10001"的权值是 1，因为只需要修改一次：对第三个字符取反即可。
现在小美拿到了一个 01 串，她希望你求出所有非空连续子串的权值之和，你能帮帮她吗？

输入例子：
10001
输出例子：
8
例子说明：
长度为 2 的子串中，有 2 个"00"的权值是 1。
长度为 3 的 3 个子串权值都是 1。
长度为 4 的 2 个子串权值都是 1。
长度为 5 的 1 个子串权值是 1。
总权值之和为 2+3+2+1=8
"""

# 没有思路，好难


def calculateWeight(s):
    totalWeight = 0
    str_len = len(s)

    for i in range(str_len - 1):
        start0, start1 = 0, 0

        # 规律：，那么从0开始的索引是偶数的下标应该都是0，从1开始的偶数
        if i % 2 == 0:
            # 如果长度是偶数，开头是0，start0 = 0，start1 = 1
            start1 += 1 if s[i] == '0' else 0
            # 长度是偶数，开头是1，start0 = 1， start1 = 0
            start0 += 1 if s[i] == '1' else 0
        else:
            # 长度是奇数，开头是0，start0 = 1， start1 = 0
            start0 += 1 if s[i] == '0' else 0
            # 长度是奇数，开头是1，start0 = 0， start1 = 1
            start1 += 1 if s[i] == '1' else 0

        for j in range(i + 1, str_len):
            if j % 2 == 0:
                start1 += 1 if s[j] == '0' else 0
                start0 += 1 if s[j] == '1' else 0
            else:
                start0 += 1 if s[j] == '0' else 0
                start1 += 1 if s[j] == '1' else 0

            totalWeight += min(start0, start1)

    return totalWeight

s = input()
result = calculateWeight(s)
print(result)