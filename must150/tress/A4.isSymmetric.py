class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        stack = [(root.left, root.right)]

        while stack:
            left, right = stack.pop()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        
        return True

       

        
