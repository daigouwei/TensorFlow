class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        if not head:
            return head
        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode
        cur = head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        return dummyNode.next
