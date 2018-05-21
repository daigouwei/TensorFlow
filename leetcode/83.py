class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return head
        pre = head
        cur = pre.next
        while cur:
            if cur.val == pre.val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return head


if __name__ == '__main__':
    head = ListNode(1)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(3)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    hh = Solution().deleteDuplicates(head)
    print(hh)
