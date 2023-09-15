# https://leetcode.cn/problems/linked-list-cycle/
# 快慢指针法，注意判断语句即可
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
        