class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        resList1 = self.readNode(l1)
        resList2 = self.readNode(l2)
        resList = []
        resList.extend(resList1)
        resList.extend(resList2)
        resList.sort()
        return self.gereateListNode(resList)

    def readNode(self, head):
        resList = []
        node = head
        while node is not None:
            resList.append(node.val)
            node = node.next
        return resList

    def gereateListNode(self, l):
        if l is None or len(l) == 0:
            return None
        head = ListNode(l[0])
        preNode = head
        for x in l[1:]:
            node = ListNode(x)
            preNode.next = node
            preNode = node
        return head


if __name__ == '__main__':
    pass
