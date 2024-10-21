# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # Initialize the variable to store the maximum path sum
        self.max_sum = float('-inf')  # Smallest possible number to start with
        
        # Recursive helper function to calculate the maximum path sum from each node
        def helper(node):
            if not node:
                return 0  # Return 0 if node is None
            
            # Recursively compute the maximum path sum for the left and right children
            # If the sum is negative, we ignore it by taking max with 0
            left_max = max(helper(node.left), 0)
            right_max = max(helper(node.right), 0)
            
            # Calculate the price of the current path passing through the node
            current_path_sum = node.val + left_max + right_max
            
            # Update the global maximum path sum
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return the maximum path sum including the current node and either left or right child
            return node.val + max(left_max, right_max)
        
        # Start the recursion from the root
        helper(root)
        
        # Return the maximum path sum found
        return self.max_sum
