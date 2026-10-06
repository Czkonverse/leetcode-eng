"""
230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

"""

"""
Mistake: Whether to use the properties of a BST ? What's the properties of a BST ? How to use it ?

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        def dfs(root, nodes):
            if root is None:
                return

            val = root.val
            nodes.append(val)

            dfs(root.left, nodes)
            dfs(root.right, nodes)

            return nodes

        res = dfs(root, [])

        return sorted(res)[k - 1]


"""
My first approach is to traverse the entire tree using DFS, store all node values in a list, sort the list, and then return the element at index k - 1.

This approach works, but it does not use the BST property.

The DFS traversal takes O(n) time, and sorting the values takes O(n log n) time, so the overall time complexity is O(n log n).
The space complexity is O(n) because I store all node values in a list, and the recursive call stack also uses O(h) space, where h is the height of the tree.

"""


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        nodes = []

        def dfs(node):
            if node is None:
                return

            nodes.append(node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        nodes.sort()

        return nodes[k - 1]


# Inorder + list
"""I can improve this by using inorder traversal.

For a BST, inorder traversal visits the nodes in ascending order because it processes the left subtree first, then the current node, and finally the right subtree.

So I can store the values during inorder traversal and directly return nodes[k - 1] without sorting.

This reduces the time complexity to O(n), because each node is visited once.

The space complexity is still O(n) because I store all node values, plus O(h) for the recursion stack.
"""


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        nodes = []

        def dfs(node):
            if node is None:
                return

            dfs(node.left)

            nodes.append(node.val)

            dfs(node.right)

        dfs(root)

        return nodes[k - 1]


# Iterative Inorder Traversal
"""
A further optimization is to use iterative inorder traversal with a stack.

I keep moving to the left and push each node onto the stack. When there is no more left child, I pop a node from the stack. Because this follows inorder traversal, each popped node is the next smallest value in the BST.

Each time I pop a node, I decrement k. When k becomes zero, I return the current node value immediately, so I do not need to traverse the rest of the tree.

The time complexity is O(h + k), because I first go down the tree to reach the smallest elements and then process nodes until I reach the kth smallest one. In the worst case, this becomes O(n).

The space complexity is O(h) for the stack. For a balanced BST, this is O(log n), while in the worst case of a skewed tree, it can be O(n).
"""


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            k -= 1

            if k == 0:
                return curr.val

            curr = curr.right
