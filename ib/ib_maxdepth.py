'''Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest 
path from the root node down to the nearest leaf node.

NOTE : The path has to end on a leaf node. 
Example :

         1
        /
       2
max depth = 2.'''


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxDepth(self, a):
        if a is None:
            return 0
        else:
            return 1+max(self.maxDepth(a.left),self.maxDepth(a.right))
