from dataclasses import dataclass, field
from typing import Any, Union

@dataclass(order=True)
class Path:
    priority: int
    path: Any=field(compare=False)


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_path_sum(self, root: Node) -> int:
        max_ = 0
        def dfs(node: Union[Node, None]) -> int:
            nonlocal max_
            if not node:
                return 0

            current = node.val
            left = dfs(node.left)
            right = dfs(node.right)
            current_max = max(left, right, current + left + right, current)
            if current_max > max_:
                max_ = current_max

            return current_max

        dfs(root)
        return max_




tree = Node(
    10,
    Node(-9),
    Node(
        -20,
        Node(-15),
        Node(-7)
    )
)

print(Solution().max_path_sum(tree))

