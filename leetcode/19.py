class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        if head is None:
            return None
        node1 = head
        m = n
        while m > 0:
            node1 = node1.next
            m -= 1
        if node1 is None:
            head = head.next
            return head
        node2 = head
        while node1.next is not None:
            node1 = node1.next
            node2 = node2.next
        if n == 1:
            node2.next = None
        else:
            node2.next = node2.next.next
        return head


if __name__ == '__main__':
    head = ListNode(1)
    node = ListNode(2)
    head.next = node
    hh = Solution().removeNthFromEnd(head, 1)
    print(hh)
