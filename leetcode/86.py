class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head, x):
        if head is None:
            return head
        head1 = None
        head2 = None
        node = head
        node1 = None
        node2 = None
        pre1 = None
        pre2 = None
        while node is not None:
            if node.val < x:
                node1 = ListNode(node.val)
                if pre1 is None:
                    head1 = node1
                else:
                    pre1.next = node1
                pre1 = node1
            else:
                node2 = ListNode(node.val)
                if pre2 is None:
                    head2 = node2
                else:
                    pre2.next = node2
                pre2 = node2
            node = node.next
        if node1 is not None:
            node1.next = head2
            return head1
        else:
            return head2
