class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def buildTree(pStart, pEnd, iStart, iEnd):

            if iStart > iEnd or pStart > pEnd:
                return None

            root = TreeNode(preorder[pStart])

            rootIndex = 0
            for i in range(iStart, iEnd+1):
                if inorder[i] == preorder[pStart]:
                    rootIndex = i
                    break
            
            leftnodecount = rootIndex - iStart 
            root.left = buildTree(pStart+1,pStart +leftnodecount,iStart,rootIndex-1 )

            root.right = buildTree(pStart+leftnodecount+1,pEnd, rootIndex+1, iEnd)

            return root

        return buildTree(0, len(preorder)-1, 0, len(inorder)-1)
        
