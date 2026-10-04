"""
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
I would solve this problem using recursion.

For each node, I recursively calculate the maximum depth of its left subtree and right subtree.

If the current node is `None`, I return `0` because an empty tree has depth zero.

Then the maximum depth of the current node is:

`1 + max(left_depth, right_depth)`

The `1` represents the current node itself.

So the code recursively computes the depth of both subtrees and returns the larger one plus one.

The time complexity is **O(n)** because every node is visited exactly once.
The space complexity is **O(h)**, where `h` is the height of the tree, because of the recursion stack. In the worst case, if the tree is completely skewed, the space complexity becomes **O(n)**.
"""


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root == None:
            return 0

        height = 0

        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        height = 1 + max(left_height, right_height)

        return height
