# 有一个长度为n的数组a，数组的和为sum=a1+a2+..+an，现在可以将一个加号变成乘号或者不变，使sum最大，求最大的sum
# 第一行输入一个整数 n，第二行输入 n 个整数表示数组 a 

# 这道题直接遍历会超时，因此需要用类似前缀和的技巧，用一个数组把所要用到的乘法与加法的差记录下来

n = int(input())
a = list(map(int, input().split()))

def countmax(n, a):
    prefix = [0] * (n-1)
    for i in range(n-1):
        prefix[i] = a[i+1] * a[i] - a[i+1] - a[i]
    return sum(a) + max(0, max(prefix))

print(countmax(n, a)) 