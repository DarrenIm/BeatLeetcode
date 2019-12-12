# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# No.100 Same Tree
class Wrong_Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p.val == None and q.val == None: # AttributeError: 'NoneType' object has no attribute 'val'
            return True
        else:
            if p.val != q.val:
                return False
            while p.val == q.val: ## 错误！ 写的很复杂，冗余code，
                pl = p.left
                pr = p.right
                ql = q.left
                qr = q.right
                if (pl == ql) and (pr == qr): # .val！！ 类无法直接用"=="比较，内存地址不同！
                    return (self.isSameTree(pl, ql) and self.isSameTree(pr, qr))
                else:
                    return False

class Correct_Solution_SameTree:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return p is q



# No.101 Symmetric Tree
class Symmetric_tree:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        stack = [(root.left, root.right)]  # stack来维护一个Node遍历队列，先进先出FIFO
        while stack:  # 判断第一次直接用"=="，后面就不会碰到了，后面都是left.left 与 right.right直接比
            left, right = stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        return True

# 104. Maximum Depth of Binary Tree
class Solution:
    def maxDepth(self, root: TreeNode) -> int: # 想复杂了，直接用递归寻找左边或右边最深的非None节点即可
        if root == None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left)) # '1+' for depth counting



# 111. Minimum Depth of Binary Tree
'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

'''
from collections import deque

class Solution_111:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        queue, level = deque([(root, 1)]), 0 # 用队列来实现BFS，找到第一个左右node都为none的节点，返回其level;速度最优
        while queue:
            node = level = queue.popleft()
            if not node.left and node.right:
                return level
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
# 另一种方法
class Solution_111_02(object):
    def minDepth(self, root): # 递归方法；若根节点的左右侧子树都不为零时（l != 0 and r != 0，取两者最小值+1；若有零，即只有左子树或右子树，或无左右子树时，depth = r + l + 1
        if not root:
            return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        return l + r + 1 if l == 0 or r == 0 else min(l, r) + 1






























