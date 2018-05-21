class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        pre = head
        cur = head.next
        newHead = None
        while cur:
            if cur == head.next and cur.val != pre.val:
                newHead = pre
                break
            if pre.val != cur.val:
                if cur.next is None or cur.next.val != cur.val:
                    newHead = cur
                    break
                pre = cur
            cur = cur.next
        if newHead is None or newHead.next is None or newHead.next.next is None:
            return newHead
        tmp = newHead
        pre = newHead
        cur = newHead.next
        while cur:
            if pre.val != cur.val:
                if cur.next is None or cur.next.val != cur.val:
                    tmp.next = cur
                    tmp = cur
                pre = cur
            cur = cur.next
        tmp.next = None
        return newHead
