class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        stack = [root]
        while stack:
            cur = stack.pop()
            if not cur:
                break
            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        
        return root
        
