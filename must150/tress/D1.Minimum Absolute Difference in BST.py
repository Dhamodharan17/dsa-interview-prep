# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        ans = 10**9
        prev =  None
        #function(1) left & right = None
        def function(root):
            nonlocal prev, ans
            if not root:
                return
            function(root.left)
            if prev:
                ans = min(ans, abs(root.val - prev.val))
            prev = root#1
            function(root.right)
        function(root)
        return ans
