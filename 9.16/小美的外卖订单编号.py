"""
美团商家的订单发起时，订单编号最开始从 1 开始，后续每发起一个订单，订单编号便在上一订单编号的基础上 +1。
为了防止订单号过大，商家还可以设置一个编号上限m，当订单编号超过m时，将又从 1 开始编号。
小美想知道，当订单编号上限为m时，第x个订单编号是多少？将有q次询问。
第一行输入一个整数q,接下来q行，每行两个整数m, x
"""

q = int(input())

def getorder(m, x):
    return  x % m if x % m != 0 else m

for i in range(q):
    m, x = map(int, input().split())
    print(getorder(m, x))