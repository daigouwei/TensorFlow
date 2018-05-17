class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        if head is None:
            return head
        endNode = None
        nodeCnt = 0
        node = head
        while node is not None:
            nodeCnt += 1
            endNode = node
            node = node.next
        # 将尾节点指向头节点
        endNode.next = head
        nodeCut = nodeCnt - k % nodeCnt
        node = head
        for i in range(nodeCut - 1):
            node = node.next
        head = node.next
        node.next = None
        return head
