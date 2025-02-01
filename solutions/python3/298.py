
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution class to solve the longest consecutive sequence problem in a binary tree
class Solution:
    # Find the length of the longest consecutive sequence path in a binary tree
    def longestConsecutive(self, root: TreeNode) -> int:
        q, l = root and [(root, 1)] or [], 0
        while q:
            node, path = q.pop()
            l = max(l, path)
            # Append children to the queue with updated path lengths if they are consecutive
            q += [(child, child.val == node.val + 1 and path + 1 or 1) for child in (node.left, node.right) if child]
        return l
