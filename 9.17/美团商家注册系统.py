"""
请你开发一个美团商家测试系统，并用等价划分法确认商家注册信息是否成功。
商家信息必须满足以下条件：
1. 系统中第一次注册的商家名字，被视为主店。
2. 系统中若出现重名商家，需要判断地址是否已存在该商家。若存在，则注册失败。否则注册成功，该商家被视为分店。
3. 商家的名字和地址必须由小写的英文字母组成，否则注册失败。
请你输出每个商家的信息，按商家名字的字典序升序输出。需要输出商家名字，商家主店地址，商家分店数量。

输入描述：
第一行输入一个正整数n，代表注册信息数量。
接下来的n行，每行输入两个字符串，用空格隔开。分别代表商家名字和商家地址。
给定的商家名字和商家地址字符串长度不超过20，且不包含空格。

输出描述：
按商家名字字典序输出全部商家信息。每行输出一个，分别输出商家名字，商家主店地址，商家分店数量，用空格隔

输入例子：
5
ranko mt
ranko op
ranko op
Ranko ok
red ok
输出例子：
ranko mt 1
red ok 0
"""
n = int(input())
businesses = {}

for _ in range(n):
    name, address = input().split()
    
    # 检查商家名字和地址是否符合要求
    if not (name.islower() and address.islower()):
        continue
    print(name, address)
    # 如果商家名字已经在字典中，检查地址是否已存在
    if name in businesses:
        if address not in businesses[name][0]:  # 地址已存在，注册失败
            businesses[name][0].append(address)
            businesses[name][1] += 1
    else:
        businesses[name] = [[address], 0]  # 注册为主店

# 对商家名字进行字典序升序排序
sorted_businesses = sorted(businesses.items())

# 输出商家信息
for name, data in sorted_businesses:
    print(f"{name} {data[0][0]} {data[1]}")