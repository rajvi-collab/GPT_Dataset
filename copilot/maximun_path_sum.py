class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root):
    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0
        
        # Calculate the maximum path sum starting from the left and right children
        left_max = max(dfs(node.left), 0)
        right_max = max(dfs(node.right), 0)
        
        # Calculate the maximum path sum passing through the current node
        current_max = node.val + left_max + right_max
        
        # Update the global maximum path sum
        max_sum = max(max_sum, current_max)
        
        # Return the maximum path sum starting from the current node
        return node.val + max(left_max, right_max)
    
    max_sum = float('-inf')
    dfs(root)
    return max_sum

# Example usage:
# root = TreeNode(1, TreeNode(2), TreeNode(3))
# print(maxPathSum(root))  # Output: 6

# root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
# print(maxPathSum(root))  # Output: 42
