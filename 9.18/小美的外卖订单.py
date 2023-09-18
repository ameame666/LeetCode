"""
小美正在设计美团外卖的定价信息。已知外卖定价的规则如下：
1. 每道菜有折扣价和原价。折扣价不能超过原价。
2. 订单有满x元减y元的优惠。当购买的菜的价格总和不小于x元时，总价格可以减y元。“减”的价格不能超过“满”的价格。
3. 满减优惠和折扣价是互斥的，当且仅当每个菜都选择了原价才可以触发满减。
4. 系统会自动为客户计算最低价格的方案。

输入描述：
第一行输入一个正整数n，代表菜的总数。
接下来的n行，每行输入两个实数a_i和b_i，代表每道菜的原价是a_i，折扣价是b_i。
最后一行输入两个实数x和y，代表满x元可以减y元。

输出描述：
如果数据有误，则输出一行字符串"error"。
否则输出一个小数，小数点后保留2位即可。该小数代表顾客购买了全部菜各一份时，订单的总价格。
"""
# 简单的模拟题，注意都是正实数，以及输出格式
import sys
n = int(input())
sum_0, sum_1 = 0, 0
for i in range(n):
    x, y = map(float, input().split())
    if y > x or y <= 0 or x <= 0:
        print('error')
        sys.exit()
    sum_0 += x
    sum_1 += y
x, y = map(float, input().split())
if y > x or y <= 0 or x <= 0:
    print('error')
    sys.exit()

if x <= sum_0:
    print("{:.2f}".format(min(sum_1, sum_0-y)))
else:
    print("{:.2f}".format(sum_1))