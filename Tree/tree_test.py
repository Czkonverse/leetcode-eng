from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])

    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        # build left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)

        i += 1

        # build right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)

        i += 1

    return root


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def dfs(node, lower, upper):
            if node is None:
                return True

            if not (lower < node.val < upper):
                return False

            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)

        return dfs(root, float("-inf"), float("inf"))


# test case 1
root = build_tree([2, 1, 3])

solution = Solution()
print(solution.isValidBST(root))  # True


# test case 2
root = build_tree([5, 1, 4, None, None, 3, 6])

print(solution.isValidBST(root))  # False
