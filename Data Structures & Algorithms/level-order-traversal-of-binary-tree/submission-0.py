from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        q = deque()
        if root:
            q.append(root)

        # add root node to FIFO q
        # in while loop, determine length of q
        # create new nested list
        # run for loop for the length of q and pop node each time from q
        # add value of node into nested list
        # after for loop add nested list into result

        while q:
            level = []

            for _ in range(len(q)):
                curr = q.popleft()
                level.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            result.append(level)
        
        return result
        