"""
小美有两个长度为n只包含小写字母的字符串s和t，小美定义“两个字符串的匹配度”为s_i =t_i​的数量，例如"abacd"和"aabdd"的匹配度就是2。
现在你可以进行最多一次以下操作:对于字符串t，选择两个索引i,j(1≤i<j≤n)，交换t_i和t_j。
小美想知道，s和t的最大字符串匹配度是多少？

输入描述：
第一行输入一个整数n
第二行输入一个长度为n的字符串s。
第三行输入一个长度为n的字符串t。

输出描述：
输出一个整数，s和t的最大匹配度。
"""
n = int(input())
s = input()
t = input()

count = 0
s_valdict = {}
t_valdict = {}

for i in range(n):
    if s[i] == t[i]:
        count += 1
    else:
        s_valdict[s[i]] = i
        t_valdict[t[i]] = i

print(count)
flag = 0
for c in s_valdict:
    if c in t_valdict:
        if t[s_valdict[c]] == s[t_valdict[c]]:
            count += 2
            flag = 1
            break
if flag == 0:
    for c in s_valdict:
        if c in t_valdict:
            count += 1
            break

print(count)