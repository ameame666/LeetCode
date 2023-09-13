# https://leetcode.cn/problems/rotate-list/
# 先遍历链表确定链表的长度，然后需要旋转的长度就是k % length，再把链表首尾相连后在需要旋转的地方断开链表，时间复杂度O(n)
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        length = 1
        cur = head
        while cur.next:
            length += 1
            cur = cur.next
        cur.next = head

        k = k % length
        
        for i in range(length - k):
            cur = cur.next

        newhead = cur.next
        cur.next = None
        return newhead
