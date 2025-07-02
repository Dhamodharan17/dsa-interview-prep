class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def tree_dfs(root):

            if not root:
                return 0

            return max(tree_dfs(root.left), tree_dfs(root.right)) + 1
        
        #return tree_dfs(root)

        def bttree_bfs(root):

            levels = 0
            if not root:
                return levels

            q = deque([root])
            while q:
                size = len(q)
                levels += 1
                for i in range(size):
                    cur = q.popleft()
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
            
            return levels


        def iterative(root):

            if not root:
                return 0
            max_height = 0

            stack = [(root,1)]
            while stack:
                cur,cur_height = stack.pop()
                max_height = max(max_height,cur_height)
                if cur.left:
                    stack.append([cur.left, cur_height+1])
                if cur.right:
                    stack.append([cur.right, cur_height+1])

            return max_height

        return iterative(root)
