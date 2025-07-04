class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        stack = [(root,str(root.val))]
        total = 0
        while stack:
            
            curr_node, curr_sum = stack.pop()
            if not curr_node.left and not curr_node.right:
                total += int(curr_sum)
                continue
            if curr_node.left:
                stack.append((curr_node.left, curr_sum+str(curr_node.left.val) ))
            if curr_node.right:
                stack.append((curr_node.right, curr_sum+str(curr_node.right.val) ))

        return total
