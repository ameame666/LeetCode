"""
给n个字符串要求看能否排序成功，要求对排好的字符串，对于所有的1<=i<j<=n，均有w_i ∈ w_j，也就是w_i是w_j的字串，如果可以，按行输出排好序的字符串，不可以就输出'NO'
"""
# 打卡题，先按长度排序，然后看前一个串是不是后一个的子串即可
n = int(input())
strs = []
for i in range(n):
    strs.append(input())

strs = sorted(strs, key=lambda x:len(x))

def substring(a, b):
    if a in b:
        return True
    else:
        return False

flag = 0
for i in range(n-1):
    if substring(strs[i], strs[i+1]):
        continue
    else:
        flag = 1
        print('No')
        break
if flag == 0:
    print('Yes')
    for c in strs:
        print(c)