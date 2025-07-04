class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return
        q = deque([root])

        while q:
            size = len(q)
            tempRightNode  = None
            for i in range(size):
                cur = q.popleft()
                cur.next = tempRightNode
              #keep changing so get right node for each node in tempRightNode
                tempRightNode = cur
              #change insertion order
                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)
        return root

        
