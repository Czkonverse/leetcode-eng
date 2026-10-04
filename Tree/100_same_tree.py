"""
100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
I would solve this problem using recursion to compare the two trees.

First, I handle the base cases. If both nodes are `None`, they are the same, so I return `True`. If only one of them is `None`, the tree structures are different, so I return `False`.

Then I compare the values of the current nodes. If `p.val` is different from `q.val`, I return `False`.

Otherwise, I recursively compare the left subtrees and the right subtrees. The two trees are the same only if both the left subtrees and the right subtrees are the same.

The time complexity is **O(n)**, where `n` is the number of nodes, because in the worst case I need to visit every node once.

The space complexity is **O(h)** because of the recursion stack, where `h` is the height of the tree. For a balanced tree, it is **O(log n)**, and in the worst case, for a skewed tree, it can be **O(n)**.
"""


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        res = False
        if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            res = True

        return res
