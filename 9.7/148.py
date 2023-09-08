# 链表排序 https://leetcode.cn/problems/sort-list/

# 使用归并排序，自顶向下，时间复杂度O(nlogn)，空间复杂度O(logn)
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def findmid(head):
            slow, fast = head, head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def merge(left, right):
            dummy = ListNode(-1)
            cur = dummy
            while left and right:
                if left.val < right.val:
                    cur.next = left
                    left = left.next
                    cur = cur.next
                else:
                    cur.next = right
                    right = right.next
                    cur = cur.next
            if left:
                cur.next = left
            if right:
                cur.next = right
            return dummy.next

        if not head or not head.next:
            return head
        
        mid = findmid(head)
        right = mid.next
        mid.next = None

        leftsort = self.sortList(head)
        rightsort = self.sortList(right)

        return merge(leftsort, rightsort)
    
# 如果使用自底向上的方法可以将空间复杂度降低到O(1)
"""
确定链表长度（find_length）： 首先，我们需要确定链表的总长度，以便后续的迭代操作。这是通过遍历整个链表并计数节点数来完成的。

迭代步长（step）： 我们从步长1开始，然后在每次迭代中将步长加倍，直到步长等于链表的长度。每一次迭代中，我们将链表拆分成若干个长度为步长的子链表，然后将它们逐一合并。

拆分链表（split）： 在每一次迭代中，我们需要将链表拆分成两个部分。拆分函数会接受一个链表头部和一个步长作为参数，然后返回第二部分链表的头部，并将第一部分链表的末尾置为None。这样，我们成功地将链表划分为两个子链表，每个子链表的长度为步长。

合并链表（merge）： 合并函数会将两个有序的子链表合并成一个有序的链表。这是一个关键操作，它确保了在每次迭代中，我们都会将两个有序的子链表合并成一个更长的有序链表。我们使用一个虚拟的头节点（dummy）来构建合并后的链表，并使用指针来追踪合并的进度。

迭代合并（迭代步长加倍）： 在每次迭代中，我们将链表拆分成越来越小的子链表，然后逐一合并这些子链表。在每次迭代结束后，步长加倍，然后继续进行下一次迭代，直到步长等于链表的长度。这个过程将重复进行，每次迭代都会使链表的有序部分增长，最终使整个链表变得有序。
"""
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getlength(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        def split(head, step):
            i = 1
            while i < step and head:
                i += 1
                head = head.next
            if not head:
                return None
            nextstart = head.next
            head.next = None
            return nextstart
        
        def merge(left, right, head):
            cur = head
            while left and right:
                if left.val < right.val:
                    cur.next = left
                    left = left.next
                else:
                    cur.next = right
                    right = right.next
                cur = cur.next
            cur.next = left if left else right
        
        if not head or not head.next:
            return head

        length = getlength(head)
        dummy = ListNode(-1)
        dummy.next = head
        step = 1

        while step < length:
            tail = dummy
            cur = dummy.next
            while cur:
                left = cur
                right = split(left, step)
                cur = split(right, step)
                merge(left, right, tail)
                while tail.next:
                    tail = tail.next
            step *= 2
        
        return dummy.next