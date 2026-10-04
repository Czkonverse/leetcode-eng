"""
226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
I use recursive DFS to invert the binary tree.

The base case is when the current node is `None`, which means this branch has reached the end.

For each node, I swap its left and right children. Then I recursively invert the left subtree and the right subtree. Since every node is processed once, the time complexity is O(n), where n is the number of nodes.

The space complexity is O(h) because of the recursion stack, where h is the height of the tree. For a balanced tree, it is O(log n), while in the worst case of a skewed tree, it becomes O(n).
"""


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:

        if root == None:
            return

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
