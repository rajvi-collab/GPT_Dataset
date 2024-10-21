# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')

        def dfs(node: TreeNode) -> int:
            """Return the maximum path sum of the subtree rooted at node."""
            if not node:
                return 0

            # Calculate the maximum path sum for the left and right subtrees
            left_sum = max(dfs(node.left), 0)
            right_sum = max(dfs(node.right), 0)

            # Update the maximum path sum if the current path sum is greater
            self.max_sum = max(self.max_sum, node.val + left_sum + right_sum)

            # Return the maximum path sum for the current node
            return node.val + max(left_sum, right_sum)

        dfs(root)
        return self.max_sum