class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        preNode = None
        cnt = 0
        nodeList = []
        node = head
        while node is not None:
            nodeList.append(node)
            cnt += 1
            if cnt == 1 and nodeList[0].next is None:
                preNode.next = nodeList[0]
                break
            if cnt == 2:
                tmp = nodeList[1].next
                nodeList[1].next = nodeList[0]
                nodeList[0].next = tmp
                if nodeList[0] == head:
                    head = nodeList[1]
                    preNode = nodeList[0]
                else:
                    preNode.next = nodeList[1]
                    preNode = nodeList[0]
                if nodeList[0].next is None:
                    break
                node = nodeList[0]
                cnt = 0
                nodeList.clear()
            node = node.next
        return head

if __name__ == '__main__':
    head = ListNode(1)
    node = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(5)
    head.next = node
    # node.next = node2
    # node2.next = node3
    # node3.next = node4
    hh = Solution().swapPairs(head)
    print(hh)
