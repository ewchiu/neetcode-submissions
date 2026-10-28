# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 

        # BFS: 1. add root to deque
        # 2. pop deque and switch pointers around
        # 3. add children to deque
        # 4. repeat
        q = deque()
        q.append(root)

        while q:
            curr = q.popleft()
            temp = curr.left
            curr.left = curr.right
            curr.right = temp

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        return root
        