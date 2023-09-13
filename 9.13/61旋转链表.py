# https://leetcode.cn/problems/rotate-list/
# 先遍历链表确定链表的长度，然后需要旋转的长度就是k % length，再把链表首尾相连后在需要旋转的地方断开链表，时间复杂度O(n)
