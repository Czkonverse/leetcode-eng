""" """


def dfs(node):
    if node is None:
        return

    dfs(node.left)
    dfs(node.right)


"""
"""


def dfs(node, 状态):
    # base case

    # 检查 / 处理当前节点

    # 左子树结果 = dfs(node.left, 新状态)
    # 右子树结果 = dfs(node.right, 新状态)

    # return 某个结果
    pass
