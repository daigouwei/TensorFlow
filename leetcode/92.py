class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def reverseBetween(self, head, m, n):
        if not head or not head.next or m == n:
            return head
        zero = ListNode(0)
        zero.next = head
        index = 0
        pre = zero
        cur = head
        start = None
        end = None
        while cur:
            index += 1
            if index == m:
                start = pre
                end = cur
            if index > m and index <= n:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
                if index == n:
                    start.next = pre
                    end.next = cur
            else:
                cur = cur.next
                pre = pre.next
        return zero.next
