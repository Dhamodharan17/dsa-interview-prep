class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False
                
        stack = [(root,targetSum-root.val)]

        while stack:
            curr_node, curr_sum = stack.pop()

            if not curr_node.left and not curr_node.right and curr_sum == 0:
                return True

            if curr_node.left:
                stack.append((curr_node.left,curr_sum-curr_node.left.val))

            if curr_node.right:
                stack.append((curr_node.right,curr_sum-curr_node.right.val))
        
        return False
