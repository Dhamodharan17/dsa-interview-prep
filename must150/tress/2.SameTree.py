class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        stack = [(p,q)]
        while stack:
            curp, curq = stack.pop()

            if not curp and not curq:
                continue
            # one of tree is shorter
            if not curp or not curq:
                return False
            # mis match in values
            if curp.val != curq.val:
                return False
            
            stack.append((curp.left, curq.left))
            stack.append((curp.right, curq.right))
        
        return True
        
        def bttree_dfs(p, q):
            
            # both trees reached end
            if not p and not q:
                return True
            # one of tree is shorter
            if not p or not q:
                return False
            # mis match in values
            if p.val != q.val:
                return False
            
            return bttree_dfs(p.left,q.left) and bttree_dfs(p.right,q.right)
        
        return bttree_dfs(p,q)
