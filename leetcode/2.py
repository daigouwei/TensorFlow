# 经验教训
# 第1次提交：使用了数值计算，发现大数值会超过int的范围，卒
# 第2次提交：改成了直接用链表求解，但是忽略了[0],[1,8]这种不对称情况，需要考虑其中一个为None时的异常
# 第3次提交：[5],[5]，有进位的这种条件也要加上

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
class Solution:
    def addTwoNumbers(self, l1, l2):
        sum = self.getVal(l1) + self.getVal(l2)
        numList = self.unfold2List(sum)
        return self.generateListNode(numList)

    def getVal(self, l):
        sum = 0
        cnt = 0
        while l != None:
            sum += l.val * (10 ** cnt)
            cnt += 1
            l = l.next
        return sum

    def unfold2List(self, num):
        numList = []
        if num == 0:
            numList = [0]
        else:
            while num > 0:
                numList.append(num % 10)
                num = int(num / 10)
        return numList

    def generateListNode(self, numList):
        numListNodeList = []
        for num in numList:
            l = ListNode(num)
            numListNodeList.append(l)
        for listNodeIndex in range(len(numListNodeList)):
            if listNodeIndex == len(numListNodeList) - 1:
                return numListNodeList[0]
            else:
                numListNodeList[listNodeIndex].next = numListNodeList[listNodeIndex + 1]
'''


class Solution:
    def addTwoNumbers(self, l1, l2):
        preNode = None
        carryFlag = 0
        preCarryFlag = 0
        while l1 != None or l2 != None or preCarryFlag == 1:
            val = (l1.val if l1 is not None else 0) + (l2.val if l2 is not None else 0) + preCarryFlag
            if val > 9:
                carryFlag = 1
                val = val % 10
            else:
                carryFlag = 0
            node = ListNode(val)
            if preNode is not None:
                preNode.next = node
            else:
                l3 = node
            preNode = node
            preCarryFlag = carryFlag
            l1 = l1.next if l1 is not None else l1
            l2 = l2.next if l2 is not None else l2
        return l3


if __name__ == '__main__':
    l1 = ListNode(5)

    l4 = ListNode(5)

    s = Solution()
    hh = s.addTwoNumbers(l1, l4)
    print(hh)
