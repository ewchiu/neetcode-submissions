# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if root:
            q.append(root)

        level = 0

        while q:
            for i in range(len(q)):
                next = q.popleft()
                if next.left:
                    q.append(next.left)
                if next.right:
                    q.append(next.right)
            level += 1
        
        return level


        
        

