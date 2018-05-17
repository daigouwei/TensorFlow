class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归写法
'''
class Solution:
    def inorderTraversal(self, root):
        if root is not None:
            self.inorderTraversal(root.left)
            print(root.val)
            self.inorderTraversal(root.right)
'''


# 迭代写法
class Solution:
    # 中序遍历
    def inorderTraversal(self, root):
        if root is None:
            return []
        res = []
        stack = []
        node = root
        while node is not None or len(stack) != 0:
            while node is not None:
                stack.append(node)
                node = node.left
            if len(stack) != 0:
                node = stack.pop()
                res.append(node.val)
                node = node.right
        return res

    # 前序遍历
    def preorderTraversal(self, root):
        if root is None:
            return []
        node = root
        res = []
        stack = []
        while node is not None or len(stack) != 0:
            while node is not None:
                res.append(node.val)
                stack.append(node)
                node = node.left
            if len(stack) != 0:
                node = stack.pop()
                node = node.right
        return res
