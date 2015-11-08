'''Given a binary tree, return the level order traversal of its nodes’ values. 
    (ie, from left to right, level by level).
    Given binary tree

        3
       / \
      9  20
        /  \
       15   7
    return its level order traversal as:

    [
      [3],
      [9,20],
      [15,7]
    ]'''


from collections import deque
class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        if A is None:
            return None
        current_level = deque([A])
        next_level = deque()
        levels = [[A.val]]
        while current_level:
            node = current_level.popleft()
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
            if not current_level:
                if next_level:
                    levels.append([n.val for n in next_level])
                current_level = next_level
                next_level = deque()
        return levels