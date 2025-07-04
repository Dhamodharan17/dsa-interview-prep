class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def builtTree(pStart, pEnd, iStart, iEnd):

            if iStart > iEnd or pStart > pEnd:
                return None
            
            root = TreeNode(postorder[pEnd])
            rootIndex = 0
            for i in range(iStart, iEnd+1):
                if inorder[i] == postorder[pEnd]:
                    rootIndex = i
                    break

            leftNodes = rootIndex - iStart
            root.left = builtTree(pStart,pStart+leftNodes-1,iStart,rootIndex-1)
            root.right = builtTree(pStart+leftNodes,pEnd -1, rootIndex+1,iEnd)

            return root
        
        return builtTree(0, len(postorder)-1,0,len(inorder)-1)
        
