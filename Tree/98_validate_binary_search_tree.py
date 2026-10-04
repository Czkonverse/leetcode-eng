"""
98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

"""

"""
Mistake: Range ? The parents ? or the children ?
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
I would solve this problem using DFS with a valid value range for each node.

For every node, I check whether its value is strictly between a lower bound and an upper bound. If it is not, the tree is not a valid BST.

When I move to the left subtree, I update the upper bound to the current node’s value. When I move to the right subtree, I update the lower bound to the current node’s value.

If I reach a null node, I return true because an empty subtree is valid.

The initial range is negative infinity to positive infinity.

The time complexity is O(n) because each node is visited once.

The space complexity is O(h), where h is the height of the tree, because of the recursion stack. For a balanced tree, this is O(log n), and in the worst case of a skewed tree, it becomes O(n).
"""


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def dfs(node, lower, upper):
            if node is None:
                return True

            if not (lower < node.val < upper):
                return False

            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)

        return dfs(root, float("-inf"), float("inf"))
