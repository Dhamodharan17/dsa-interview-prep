# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = -10**9
        def function(root):
            nonlocal maxi
            if not root:
                return 0
              
            left = max(0,function(root.left))
            right = max(0,function(root.right))

            #subtree path
            #we already removed -ve so it will give max
            maxi = max(maxi, left+right+root.val)
            # nominate best path among themselves, we removed -ve so root can be also returned.
            return max(left, right) + root.val

          
        function(root)
        return maxi 
